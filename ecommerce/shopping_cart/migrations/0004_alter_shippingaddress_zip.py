# Generated by Django 5.0 on 2024-09-02 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0003_alter_shippingaddress_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='zip',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(100)]),
        ),
    ]
