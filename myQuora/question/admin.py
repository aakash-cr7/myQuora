from django.contrib import admin
from .models import Question, Topic, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'by')

# Register your models here.
admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
