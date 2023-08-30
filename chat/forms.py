from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, SupportAgent

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField() 
    class Meta:
        model = Customer
        fields = ['username', 'password1', 'password2', 'phone_number']

class SupportAgentRegistrationForm(UserCreationForm):
    class Meta:
        model = SupportAgent
        fields = []