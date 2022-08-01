# Generated by Django 4.0.6 on 2022-07-24 08:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appx', '0010_rename_timeline_time_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_line',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('0', 'zeroth review'), ('1', 'first review'), ('2', 'second review'), ('3', 'third review'), ('4', 'fourth review')], max_length=9, null=True),
        ),
    ]