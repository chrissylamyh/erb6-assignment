# Generated by Django 5.2.3 on 2025-06-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income_expense', '0002_alter_income_options_alter_income_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': 'Income', 'verbose_name_plural': 'Income Records'},
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
