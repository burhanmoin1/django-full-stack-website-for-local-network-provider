from django.contrib import admin
from .models import UserInput

# Register your models here.
class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_complaint')

admin.site.register(UserInput, CustomerFeedbackAdmin)