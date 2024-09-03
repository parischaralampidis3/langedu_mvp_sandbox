# Generated by Django 5.0.7 on 2024-09-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_enrollment"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseMaterial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_material_title", models.CharField(max_length=100)),
                ("course_material_description", models.CharField(max_length=100)),
                ("course_material_difficulty", models.CharField(max_length=100)),
                ("course_material_isActive", models.BooleanField(default=True)),
                ("course_material_category", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
