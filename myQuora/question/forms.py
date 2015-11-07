from django import forms
from .models import Question, Topic, Answer

class addQuestionForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset = Topic.objects.all())
    class Meta:
        model = Question
        fields = ['title', 'desc']
