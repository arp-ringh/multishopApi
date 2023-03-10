# Generated by Django 4.1.3 on 2022-11-02 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=400)),
                ("email", models.EmailField(blank=True, max_length=400)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Slider",
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
                ("name", models.CharField(max_length=300)),
                ("image", models.ImageField(upload_to="slider")),
                ("url", models.CharField(max_length=500)),
                ("rank", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("active", "active"), ("", "default")],
                        max_length=100,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
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
                ("name", models.CharField(max_length=300)),
                (
                    "rank",
                    models.CharField(
                        choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
                        max_length=50,
                    ),
                ),
                ("image", models.ImageField(upload_to="offer")),
                (
                    "offer_products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]
