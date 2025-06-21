from django.db import models

class Income(models.Model):
    amount = models.DecimalField(verbose_name='Amount', max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name='Date')
    description = models.CharField(verbose_name='Narrations', max_length=255)
    
    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Income Records'
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.source} - {self.amount}"

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"

class Investment(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    return_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.type} - {self.amount}"
