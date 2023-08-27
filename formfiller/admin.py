from django.contrib import admin
from .models import UserInput

@admin.register(UserInput)
class UserInputAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_complaint')
