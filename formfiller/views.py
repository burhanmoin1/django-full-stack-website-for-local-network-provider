from django.shortcuts import render, redirect
from .models import UserInput

def input_form(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_complaint = request.POST.get('customer_complaint')
        customer_email = request.POST.get('customer_email')
        
        # Create and save a new UserInput object
        UserInput.objects.create(
            customer_name=customer_name,
            customer_complaint=customer_complaint,
            customer_email=customer_email
        )
        # Redirect to the same page to clear the form
    
    return render(request, 'input_form.html')


def display_data(request):
    user_inputs = UserInput.objects.all()
    return render(request, 'display_data.html', {'user_inputs': user_inputs})

def homepage(request):
    return render(request,'home.html')

def internet_page(request):
    return render(request, 'internet_page.html')

def contact_page(request):
    return render(request, 'input_form.html')
