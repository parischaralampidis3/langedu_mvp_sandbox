# Generated by Django 4.1.5 on 2024-07-28 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0004_alter_student_options_remove_student_date_joined_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="password",
        ),
    ]
