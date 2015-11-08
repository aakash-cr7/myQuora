from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template import loader
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import LoginForm, SignupForm, ForgotPasswordForm
from .models import CustomUser

# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f = LoginForm()
    else: # for POST request
        f = LoginForm(request.POST)
        if f.is_valid():
            user = f.get_user()
            auth_login(request, user)
            return redirect('home')
    return render(request, 'authentication/login.html', { 'form': f })

@require_GET
def logout(request):
    auth_logout(request)
    return redirect('login')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f = SignupForm()
    else:
        f = SignupForm(request.POST)
        if f.is_valid():
            user = f.save()
            # Send verification email as well
            email_body_context = {
                'username': user.username,
                'token': urlsafe_base64_encode(force_bytes(user.username)), # As encode func takes bytes not string
                'uid': user.id,
                'protocol': 'https' if settings.USE_HTTPS else 'http',
                'domain': get_current_site(request).domain,
            }
            body = loader.render_to_string('authentication/signup_email_body_text.html', email_body_context)
            subject = 'Welcome to MyQuora'
            email_message = EmailMultiAlternatives(subject, body, settings.DEFAULT_FROM_EMAIL, [user.email])
            email_message.send()
            return render(request, 'authentication/signup_email_sent.html', { 'email': user.email })
    return render(request, 'authentication/signup.html', { 'form': f })

@require_GET
@login_required
def home(request):
    return render(request, 'base/loggedin.html')

@require_GET
def activate(request, uid = None, token = None):
    if request.user.is_authenticated():
        return redirect('home')
    '''
    try:
        user = CustomUser.objects.get(id = uid)
    except CustomUser.DoesNotExist:
        raise Http404('Invalid User')
    '''
    user = get_object_or_404(CustomUser, id = uid)
    username_from_token = force_text(urlsafe_base64_decode(token))
    if user.is_active:
        return redirect('login')

    if user.username == username_from_token:
        user.is_active = True
        user.save()
        return render(request, 'authentication/activation_success.html')
    else:
        return render(request, 'authentication/activation_failure.html')

