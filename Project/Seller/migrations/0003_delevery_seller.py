# Generated by Django 4.1.5 on 2023-02-02 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_alter_newuser_password_alter_seller_password'),
        ('Seller', '0002_remove_delevery_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='delevery',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.seller'),
        ),
    ]
