# Generated by Django 2.0.3 on 2018-09-19 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0065_product_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariantQuotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='productvariantquotation',
            name='quotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Quotation'),
        ),
        migrations.AddField(
            model_name='productvariantquotation',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.ProductVariant'),
        ),
    ]