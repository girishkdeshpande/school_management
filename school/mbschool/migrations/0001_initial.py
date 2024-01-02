# Generated by Django 5.0 on 2023-12-30 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('enrolled_year', models.DateField(verbose_name='admission date')),
                ('student_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20, unique=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbschool.student')),
            ],
        ),
    ]
