# Generated by Django 4.0.2 on 2022-02-22 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='deadline',
        ),
    ]
