# Generated by Django 3.2 on 2021-08-13 09:29

from django.db import migrations, models
import parking_permits_app.models.parking_permit


class Migration(migrations.Migration):

    dependencies = [
        ("parking_permits_app", "0014_move_zone_to_address_add_identifier_to_permit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parkingpermit",
            name="identifier",
            field=models.IntegerField(
                db_index=True,
                default=parking_permits_app.models.parking_permit.get_next_identifier,
                editable=False,
                unique=True,
            ),
        ),
    ]