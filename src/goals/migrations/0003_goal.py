# Generated by Django 5.0.6 on 2024-06-24 16:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goals", "0002_rename_id_deleted_goalcategory_is_deleted"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Goal",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "К выполнению"),
                            (2, "В процессе"),
                            (3, "Выполнено"),
                            (4, "Архив"),
                        ],
                        default=1,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "priority",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Низкий"),
                            (2, "Средний"),
                            (3, "Высокий"),
                            (4, "Критический"),
                        ],
                        default=2,
                        verbose_name="Приоритет",
                    ),
                ),
                (
                    "due_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата выполнения"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="goals",
                        to="goals.goalcategory",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="goals",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Цель",
                "verbose_name_plural": "Цели",
            },
        ),
    ]