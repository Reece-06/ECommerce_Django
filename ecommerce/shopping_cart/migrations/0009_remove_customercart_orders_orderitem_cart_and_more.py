# Generated by Django 5.0 on 2024-09-04 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0008_alter_shippingaddress_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customercart',
            name='orders',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.customercart'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_ordered',
            field=models.DateField(auto_now=True),
        ),
    ]
