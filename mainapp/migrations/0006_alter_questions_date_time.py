# Generated by Django 4.1.7 on 2023-03-17 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_questions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 17, 17, 52, 21, 523512)),
        ),
    ]
