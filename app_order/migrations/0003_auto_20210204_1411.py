# Generated by Django 3.1.4 on 2021-02-04 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0002_remove_order_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order Item', 'verbose_name_plural': 'Order Items'},
        ),
    ]
