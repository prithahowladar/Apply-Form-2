# Generated by Django 2.0.13 on 2020-04-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_userinfo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo1',
            name='degree',
            field=models.BooleanField(default=False),
        ),
    ]