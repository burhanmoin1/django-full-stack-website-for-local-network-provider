from django import forms
from .models import UserInput

class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['customer_name', 'customer_complaint', 'customer_email']
