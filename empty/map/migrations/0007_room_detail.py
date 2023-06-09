# Generated by Django 4.2.1 on 2023-06-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0006_room_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room_detail",
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
                ("rent_type", models.CharField(max_length=50)),
                ("area", models.FloatField()),
                ("location", models.CharField(max_length=100)),
                ("room_type", models.CharField(max_length=50)),
                ("maintenance_fee", models.IntegerField(blank=True, null=True)),
                ("parking_fee", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("floor", models.IntegerField(blank=True, null=True)),
                ("size", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
