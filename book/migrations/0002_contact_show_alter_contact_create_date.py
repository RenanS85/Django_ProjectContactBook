# Generated by Django 4.0.4 on 2022-07-04 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 19, 38, 47, 997305, tzinfo=utc)),
        ),
    ]
