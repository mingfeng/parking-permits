# Generated by Django 3.2 on 2021-08-26 07:38
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parking_permits_app", "0017_add_status_field_in_parking_permit_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="id",
            field=models.TextField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="street_name_sv",
            field=models.CharField(
                default="", max_length=128, verbose_name="Street name sv"
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, null=True, srid=4326, verbose_name="Location (2D)"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="id",
            field=models.TextField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="national_id_number",
            field=models.CharField(
                blank=True,
                max_length=16,
                null=True,
                verbose_name="National identification number",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="primary_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.PROTECT,
                related_name="customers_primary_address",
                to="parking_permits_app.address",
                verbose_name="Primary address",
            ),
        ),
    ]