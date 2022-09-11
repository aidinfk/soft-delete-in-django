# Generated by Django 4.1.1 on 2022-09-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
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
                    "is_deleted",
                    models.BooleanField(blank=True, editable=False, null=True),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
