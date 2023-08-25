from django.shortcuts import render, redirect
from .forms import UserFeedbackForm
from .models import UserInput

def input_form(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you_page')  # Redirect to a thank you page
    else:
        form = UserInput()
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
