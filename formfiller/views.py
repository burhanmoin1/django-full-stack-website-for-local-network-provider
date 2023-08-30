from django.shortcuts import render, redirect
from .forms import UserFeedbackForm, SignupForm
from .models import UserInput

def feedback_form_view(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank you page
    else:
        form = UserInput()
        # Redirect to the same page to clear the form
    context = {'form': form}
    return render(request, 'input_form.html', context)

def submit_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = SignupForm()
    return render(request, "signup_form.html", {"form": form})


def homepage(request):
    return render(request,'home.html')

def internet_page(request):
    return render(request, 'internet_page.html')

def contact_page(request):
    return render(request, 'input_form.html')

def thank_you(request):
    return render(request,'thank_you.html')

def tv_page(request):
    return render(request, 'tv.html')
