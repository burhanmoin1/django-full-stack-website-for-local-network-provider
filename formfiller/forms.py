from django import forms
from .models import UserInput, Signup

class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['customer_name', 'customer_complaint', 'customer_email']

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('full_name', 'package_interested', 'home_address', 'phone_number')