# Generated by Django 5.1.1 on 2025-01-22 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
    ]
