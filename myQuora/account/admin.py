from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # Which fields to ask while creating new user manually
    # fields = ('username', 'email')
    list_display = ('username', 'email')

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
