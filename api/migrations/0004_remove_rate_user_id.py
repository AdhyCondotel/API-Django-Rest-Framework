# Generated by Django 2.0 on 2019-03-30 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rate_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='user_id',
        ),
    ]
