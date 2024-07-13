# Generated by Django 5.0.7 on 2024-07-13 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_productimages_options_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='shop.colorimages'),
        ),
    ]
