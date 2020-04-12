# Generated by Django 2.0.13 on 2020-04-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255, null=True)),
                ('profile', models.CharField(max_length=255, null=True)),
                ('vacancy', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]