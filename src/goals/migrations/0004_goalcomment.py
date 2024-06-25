# Generated by Django 5.0.6 on 2024-06-25 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goals", "0003_goal"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GoalComment",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст")),
                (
                    "goal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="goals.goal",
                        verbose_name="Цель",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
    ]
