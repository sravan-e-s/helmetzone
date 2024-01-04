# Generated by Django 4.1.5 on 2023-02-07 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0004_productt'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_quantity', models.IntegerField(default=1)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.productt')),
            ],
        ),
    ]
