# Generated by Django 3.1 on 2020-08-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.BooleanField(choices=[(True, 'Boast'), (False, 'Roast')]),
        ),
    ]
