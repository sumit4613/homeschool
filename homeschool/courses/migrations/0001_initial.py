# Generated by Django 3.0.2 on 2020-05-10 01:55

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("schools", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "days_of_week",
                    models.PositiveIntegerField(
                        default=31, help_text="The days of the week when this runs"
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4)),
                (
                    "grade_levels",
                    models.ManyToManyField(
                        related_name="courses", to="schools.GradeLevel"
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="CourseTask",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4)),
                ("description", models.TextField()),
                (
                    "duration",
                    models.PositiveIntegerField(
                        help_text="The expected length of the task in minutes"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_tasks",
                        to="courses.Course",
                    ),
                ),
            ],
            options={"ordering": ("order",), "abstract": False},
        ),
        migrations.CreateModel(
            name="GradedWork",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course_task",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="graded_work",
                        to="courses.CourseTask",
                    ),
                ),
            ],
        ),
    ]
