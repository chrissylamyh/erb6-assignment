from django.contrib import admin
from .models import Income, Expense, Investment

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Investment)

admin.site.site_header = 'Annual income & expenditure'
admin.site.site_title = 'Annual income & expenditure'
admin.site.index_title = 'Welcome to Annual income & expenditure'
