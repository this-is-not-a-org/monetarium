from django.contrib import admin
from . import models

admin.site.register(models.Card)
admin.site.register(models.FinanceIncome)
admin.site.register(models.Savings)
