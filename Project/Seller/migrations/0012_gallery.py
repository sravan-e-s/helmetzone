# Generated by Django 4.1.5 on 2023-02-24 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0011_workassign'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='galleryDocs/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.productt')),
            ],
        ),
    ]