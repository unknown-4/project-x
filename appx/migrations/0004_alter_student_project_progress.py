# Generated by Django 4.0.6 on 2022-07-23 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appx', '0003_alter_student_project_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='project_progress',
            field=models.IntegerField(blank=True, default=0, max_length=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
