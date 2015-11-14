from django import forms
from .models import Question, Topic, Answer

class QuestionCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionCreateForm, self).__init__(*args, **kwargs)
        self.fields['desc'].label = 'Description'
        self.fields['topics'].required = True

    class Meta:
        model = Question
        fields = ['title', 'desc', 'topics']

class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Answer'

    class Meta:
        model = Answer
        fields = ['text']

