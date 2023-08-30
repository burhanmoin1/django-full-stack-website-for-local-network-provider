from django.shortcuts import render, redirect
from .models import Customer, SupportAgent, Ticket, Message
from django.contrib.auth.decorators import login_required
from .forms import SupportAgentRegistrationForm, CustomerRegistrationForm
from django.contrib.auth import login, logout

@login_required
def customer_dashboard(request):
    customer = request.user.customer
    tickets = Ticket.objects.filter(customer=customer)
    return render(request, 'customer_dashboard.html', {'tickets': tickets})

@login_required
def support_agent_dashboard(request):
    support_agent = request.user.supportagent
    open_tickets = Ticket.objects.filter(support_agent=support_agent, status='open')
    return render(request, 'support_agent_dashboard.html', {'open_tickets': open_tickets})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        customer = request.user.customer
        ticket = Ticket.objects.create(subject=subject, customer=customer)
        return redirect('customer_dashboard')
    return render(request, 'create_ticket.html')

@login_required
def view_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    messages = Message.objects.filter(ticket=ticket)
    
    if request.user.is_customer:
        template_name = 'customer_view_ticket.html'
    else:
        template_name = 'admin_view_ticket.html'

    return render(request, template_name, {'ticket': ticket, 'messages': messages})

@login_required
def reply_to_ticket(request, ticket_id):
    if request.method == 'POST':
        ticket = Ticket.objects.get(id=ticket_id)
        content = request.POST['content']
        sender = request.user
        message = Message.objects.create(ticket=ticket, sender=sender, content=content)
        return redirect('view_ticket', ticket_id=ticket_id)
    return render(request, 'reply_to_ticket.html', {'ticket_id': ticket_id})

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'registration/customer_register.html', {'form': form})

def support_agent_register(request):
    if request.method == 'POST':
        form = SupportAgentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('support_agent_dashboard')
    else:
        form = SupportAgentRegistrationForm()
    return render(request, 'registration/support_agent_register.html', {'form': form})

def home(request):
    return render(request, 'home2.html')