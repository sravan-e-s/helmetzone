# Generated by Django 4.1.5 on 2023-02-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
