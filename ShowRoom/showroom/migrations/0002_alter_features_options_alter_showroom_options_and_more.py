# Generated by Django 4.2.3 on 2023-07-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="features",
            options={"verbose_name_plural": "Features"},
        ),
        migrations.AlterModelOptions(
            name="showroom",
            options={"verbose_name_plural": "ShowRooms"},
        ),
        migrations.AlterModelOptions(
            name="staff",
            options={"verbose_name_plural": "Staff"},
        ),
        migrations.AddField(
            model_name="engine",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
