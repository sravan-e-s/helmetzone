# Generated by Django 4.1.5 on 2023-02-09 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_cart'),
        ('Seller', '0004_productt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workassign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.booking')),
                ('dboy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.delevery')),
            ],
        ),
    ]
