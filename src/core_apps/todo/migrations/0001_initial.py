# Generated by Django 4.2.9 on 2024-12-02 10:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoTasks",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Title of the Task"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Description of the Task"
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Todo App",
                "verbose_name_plural": "Todo Apps",
            },
        ),
    ]
