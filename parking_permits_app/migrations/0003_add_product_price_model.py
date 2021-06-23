# Generated by Django 3.2 on 2021-06-21 08:45

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parking_permits_app", "0002_add_default_shared_product_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="end_date",),
        migrations.RemoveField(model_name="product", name="price",),
        migrations.RemoveField(model_name="product", name="start_date",),
        migrations.CreateModel(
            name="ProductPrice",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Time created"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Time modified"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=6, verbose_name="Product price"
                    ),
                ),
                ("start_date", models.DateField(verbose_name="Start date")),
                (
                    "end_date",
                    models.DateField(blank=True, null=True, verbose_name="End date"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="prices",
                        to="parking_permits_app.product",
                        verbose_name="Product price",
                    ),
                ),
            ],
            options={
                "verbose_name": "Price",
                "verbose_name_plural": "Prices",
                "db_table": "price",
            },
        ),
    ]