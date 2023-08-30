from django.db import models
from django import forms

class UserInput(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_complaint = models.TextField()
    customer_email = models.EmailField()

    def __str__(self):
        return self.customer_name
    
class Signup(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic'),
        ('thunder', 'Thunder'),
        ('storm', 'Storm'),
        ('flash', 'Flash'),
        ('void', 'Void'),
    ]

    full_name = models.CharField(max_length=100)
    package_interested = models.CharField(max_length=10, choices=PACKAGE_CHOICES)
    home_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name