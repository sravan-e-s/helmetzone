# Generated by Django 4.1.5 on 2023-02-21 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_remove_feedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='seller',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feedback',
            name='seller',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.IntegerField(default=0),
        ),
    ]
