from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    monthly_income = models.DecimalField(max_digits=12, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    approved_limit = models.IntegerField(default=0)
    current_debt = models.DecimalField(max_digits=12, decimal_places=2, default=0)
