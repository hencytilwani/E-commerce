# Generated by Django 4.2.5 on 2023-09-29 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_order_itemsprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
    ]
