# Generated by Django 4.2.1 on 2023-06-14 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_customuser_id_alter_customuser_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="username",
        ),
    ]