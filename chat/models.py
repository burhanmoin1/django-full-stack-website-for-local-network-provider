from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'user'
    # Add other customer-specific fields

    def __str__(self):
        return self.user.username

class SupportAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    USERNAME_FIELD = 'user'
    # Add other support agent-specific fields

    def __str__(self):
        return self.user.username

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    support_agent = models.ForeignKey(SupportAgent, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')], default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.sender.username} - {self.timestamp}'
