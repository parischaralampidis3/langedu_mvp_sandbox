# Generated by Django 5.0.7 on 2024-09-10 20:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0003_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="text_question",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="dashboard.textquestion"
            ),
        ),
    ]
