# Generated by Django 4.1.5 on 2023-01-10 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daily_quotas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyquota",
            name="sleep",
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]