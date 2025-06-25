from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Income, Expense, Investment
from import_export import resources, fields, widgets
from datetime import datetime

class IncomeResource(resources.ModelResource):
    date = fields.Field(attribute='date', column_name='date')
    def clean_date(self, value):
        formats = ['%Y/%m/%d', '%Y-%m/%d', '%d-%b-%y']
        for fmt in formats:
            try:
                return datetime.strptime(value, fmt).date()
            except (ValueError, TypeError):
                continue
        raise ValueError(f"無法將日期 '{value}' 解析為有效格式。")
    class Meta:
        model = Income
        import_id_fields = ('id',)
        fields = ('id', 'user', 'date', 'source', 'amount', 'description')

@admin.register(Income)
class IncomeAdmin(ImportExportModelAdmin):
    resource_class = IncomeResource
    list_display = ('date', 'source', 'amount', 'description', 'user')
    list_filter = ('date', 'source', 'user')
    search_fields = ('source', 'description')
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

class ExpenseResource(resources.ModelResource):
    date = fields.Field(attribute='date', column_name='date')
    def clean_date(self, value):
        formats = ['%d-%b-%y', '%Y/%m/%d', '%Y-%m-%d']
        for fmt in formats:
            try:
                return datetime.strptime(value, fmt).date()
            except (ValueError, TypeError):
                continue
        raise ValueError(f"無法將日期 '{value}' 解析為有效格式。")
    class Meta:
        model = Expense
        import_id_fields = ('id',)
        fields = ('id', 'user', 'date', 'category', 'amount', 'description')
        skip_unchanged = True
        report_skipped = True

@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    resource_class = ExpenseResource
    list_display = ('date', 'category', 'amount', 'description', 'user')
    list_filter = ('date', 'category', 'user')
    search_fields = ('category', 'description')
    ordering = ['date']
