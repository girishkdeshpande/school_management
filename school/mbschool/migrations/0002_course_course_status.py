# Generated by Django 5.0 on 2023-12-31 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbschool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_status',
            field=models.BooleanField(default=True),
        ),
    ]
