from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(verbose_name='Date')
    source = models.CharField(verbose_name='Source', max_length=100)
    amount = models.DecimalField(verbose_name='Amount', max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name='Description', blank=True)

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Income Records'

    def __str__(self):
        return f"{self.date} - {self.source} - {self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    investment_type = models.CharField(verbose_name='Investment Type', max_length=100, default='')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    return_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.investment_type} - {self.amount}"
