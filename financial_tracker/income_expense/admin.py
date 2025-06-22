from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Income, Expense, Investment

@admin.register(Income)
class IncomeAdmin(ImportExportModelAdmin):
    list_display = ('date', 'source', 'amount', 'description', 'user')
    list_filter = ('date', 'source', 'user')
    search_fields = ('source', 'description')
    ordering = ['date']

@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    list_display = ('date', 'category', 'amount', 'description', 'user')
    list_filter = ('date', 'category', 'user')
    search_fields = ('category', 'description')
    ordering = ['date']

@admin.register(Investment)
class InvestmentAdmin(ImportExportModelAdmin):
    list_display = ('date', 'investment_type', 'amount', 'return_rate', 'description', 'user')
    list_filter = ('date', 'investment_type', 'user')
    search_fields = ('investment_type', 'description')
    ordering = ['date']

admin.site.site_header = "Financial Tracker Admin"
admin.site.site_title = "Financial Tracker Admin Portal"
admin.site.index_title = "Welcome to Financial Tracker Portal"
