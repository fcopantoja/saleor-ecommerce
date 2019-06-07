# Generated by Django 2.0.3 on 2019-06-07 00:25

from django.db import migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_rename_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='discount_amount',
            field=django_prices.models.MoneyField(currency='MXN', decimal_places=2, default=0, max_digits=12),
        ),
    ]
