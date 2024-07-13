# Generated by Django 5.0.7 on 2024-07-13 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'Mahsulot rasmlari', 'verbose_name_plural': 'Mahsulot Rasmi'},
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount_items', to='shop.discounts', verbose_name='Chegirmasi'),
        ),
    ]
