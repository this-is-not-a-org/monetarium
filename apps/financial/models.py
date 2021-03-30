from django.conf import settings
from django.db import models
from django.urls import reverse_lazy


class Card(models.Model):
    CARD_TYPE_CHOICES = [
        ('CR', 'Crédito'),
        ('DE', 'Débito'),
    ]  
    name = models.CharField(max_length=255)
    card_type = models.CharField(max_length=2, choices=CARD_TYPE_CHOICES, default='CR')
    limit = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name


class FinanceIncome(models.Model):
    FINANCE_INCOME_TYPE_CHOICES = [
        ('DV', 'Dívida'),
        ('DVR', 'Dívida recorrentes'),
        ('DVC', 'Dívida com cartão'),
        ('DS', 'Dinheiro separado'),
        ('RR', 'Renda recorrente'),
        ('RA', 'Renda adicional'),
    ]
    name = models.CharField(max_length=255)
    tipo = models.CharField(max_length=3, choices=FINANCE_INCOME_TYPE_CHOICES, default='DV')
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
        return self.name


class Savings(models.Model):
    name = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    goal = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name
