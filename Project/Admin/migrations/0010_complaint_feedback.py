# Generated by Django 4.1.5 on 2023-02-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_delete_complaint_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=400)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.IntegerField(default=0)),
                ('seller', models.IntegerField(default=0)),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_replay', models.CharField(default='not viewd yet', max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0)),
                ('seller', models.IntegerField(default=0)),
                ('feedback', models.CharField(max_length=300)),
            ],
        ),
    ]
