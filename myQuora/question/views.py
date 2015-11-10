from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import QuestionCreateForm
from .models import Question, Answer, Topic

# Create your views here.

@login_required
@require_http_methods(['GET', 'POST'])
def create_question(request):
    if request.method == 'GET':
        f = QuestionCreateForm()
    else:
        f = QuestionCreateForm(request.POST)
        if f.is_valid():
            q = f.save(commit = False)
            q.by = request.user
            q.save()
            f.save_m2m() # For saving Topics
            return redirect('myquestions')
    return render(request, 'questions/create.html', { 'form': f })

@login_required
@require_GET
def myquestions(request, page_num = 1):
    questions = Question.objects.filter(by = request.user).order_by('-created_at')
    p = Paginator(questions, 5)
    current_page = p.page(page_num)
    context = {
        'questions': current_page.object_list,
        'page': current_page,
    }
    return render(request, 'questions/myquestions.html', context)

@login_required
@require_GET
def search(request):
    query_term = request.GET.get('q')
    data = {'question': []}
    if not query_term:
        return JsonResponse(data)
    questions = Question.objects.filter(
        Q(title__icontains = query_term) | Q(desc__icontains = query_term)
    )
    data['question'] = [ {'id': q.id, 'title': q.title} for q in questions ]
    print(data)
    return JsonResponse(data)
