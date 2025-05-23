# Generated by Django 5.1.7 on 2025-04-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventorySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_stock_threshold', models.PositiveIntegerField(default=5)),
            ],
            options={
                'verbose_name_plural': 'Inventory Settings',
            },
        ),
    ]
