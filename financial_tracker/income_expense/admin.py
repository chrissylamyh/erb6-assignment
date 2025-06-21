from django.contrib import admin
from .models import Income, Expense, Investment

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Investment)
