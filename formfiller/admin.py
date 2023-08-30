from django.contrib import admin
from .models import UserInput, Signup

admin.site.register(Signup)


@admin.register(UserInput )
class UserInputAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_complaint')
