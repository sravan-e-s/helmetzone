# Generated by Django 4.1.5 on 2023-01-30 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_delete_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='helmetModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.brand')),
            ],
        ),
    ]