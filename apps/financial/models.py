from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.urls import reverse_lazy


class Planning(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=650)
    init_date = models.DateField()
    final_date = models.DateField()
    user = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Card(models.Model):
    CARD_TYPE_CHOICES = [
        ('CC', 'Credit card'),
        ('DC', 'Debit card'),
    ]  
    name = models.CharField(max_length=255)
    card_type = models.CharField(max_length=2, choices=CARD_TYPE_CHOICES, default='CR')
    limit = models.DecimalField(max_digits=20, decimal_places=2)
    user = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FinanceIncome(models.Model):
    FINANCE_INCOME_TYPE_CHOICES = [
        ('DB', 'Debt'),
        ('RD', 'Recurring debt'),
        ('CD', 'Card debt'),
        ('SM', 'Separate money'),
        ('RI', 'Recurring income'),
        ('AI', 'Additional income'),
    ]
    name = models.CharField(max_length=255)
    income_type = models.CharField(max_length=3, choices=FINANCE_INCOME_TYPE_CHOICES, default='DV')
    value = models.DecimalField(max_digits=20, decimal_places=2)
    user = ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Saving(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    goal = models.DecimalField(max_digits=20, decimal_places=2)
    user = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
