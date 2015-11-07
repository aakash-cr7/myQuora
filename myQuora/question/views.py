from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import addQuestionForm
from .models import Question

# Create your views here.

@login_required
@require_http_methods(['GET', 'POST'])
def addQuestion(request):
    if request.method == 'GET':
        f = addQuestionForm()
    else:
        f = addQuestionForm(request.POST)
        if f.is_valid():
            ques = f.save(commit = False)
            ques.by = request.user
            ques.save()
            return redirect('home')
    return render(request, 'base/addQuestion.html', { 'form': f })

@require_GET
def question_info(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, 'base/questionInfo.html', { 'ques' : question })
