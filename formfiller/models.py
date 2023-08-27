from django.db import models

class UserInput(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_complaint = models.TextField()
    customer_email = models.EmailField()

    def __str__(self):
        return self.customer_name
