# Generated by Django 2.0.13 on 2020-04-10 16:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20200408_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=1024, null=True, verbose_name='Name of the College')),
                ('university', models.CharField(max_length=1024, null=True, verbose_name='Name of the University')),
                ('unicityandstate', models.CharField(max_length=1024, null=True, verbose_name='Uni City and State')),
                ('degree', models.NullBooleanField()),
                ('field', models.CharField(max_length=1024, null=True, verbose_name='Field of study')),
                ('graduationyear', models.FloatField(default=2020, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(2025)], verbose_name='Graduation year')),
                ('highschool', models.CharField(max_length=1024, null=True, verbose_name='Name of the High School')),
                ('hspercentage', models.CharField(max_length=10, null=True, verbose_name='high school percentage')),
                ('hsyear', models.FloatField(default=2020, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(2025)], verbose_name='High School Graduation year')),
                ('hscityandstate', models.CharField(max_length=1024, null=True, verbose_name='HS City and State')),
                ('ssschool', models.CharField(max_length=1024, null=True, verbose_name='Name of the SS School')),
                ('sspercentage', models.CharField(max_length=10, null=True, verbose_name='ss school percentage')),
                ('ssyear', models.FloatField(default=2020, validators=[django.core.validators.MaxValueValidator(2000), django.core.validators.MinValueValidator(2025)], verbose_name='ss School Graduation year')),
                ('sscityandstate', models.CharField(max_length=1024, null=True, verbose_name='ss City and State')),
            ],
        ),
    ]
