# Generated by Django 5.1.1 on 2025-01-22 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='created',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
    ]
