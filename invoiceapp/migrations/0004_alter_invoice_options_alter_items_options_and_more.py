# Generated by Django 4.0.4 on 2022-05-05 07:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0003_alter_items_item_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': 'Invoice', 'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name': 'Items', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_address',
            field=models.TextField(blank=True, null=True, verbose_name='Customer Address'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_name',
            field=models.CharField(max_length=200, verbose_name='Customer Name'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer_phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Customer Phone'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(auto_now_add=True, verbose_name='Invoice Date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='Invoice ID'),
        ),
    ]
