# Generated by Django 3.2.8 on 2021-11-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0002_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
