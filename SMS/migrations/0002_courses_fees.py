# Generated by Django 3.2.6 on 2021-08-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='fees',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
