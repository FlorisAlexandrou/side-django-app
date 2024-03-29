# Generated by Django 5.0.2 on 2024-03-02 08:46

import csv
from datetime import datetime
from django.db import migrations


def populate_from_csv(apps, schema_editor):
    # Use historical version of Person model to avoid potential version conflicts in this migration.
    Client = apps.get_model("mat_app", "Client")
    with open("mat_app/data/hanki-panki-test-data-2k.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Client.objects.create(
                first_name=row['First Name'],
                last_name=row['Last Name'],
                address=row['Address'],
                date_of_birth=datetime.strptime(row['DoB'], '%d-%m-%Y').date(),
            )


class Migration(migrations.Migration):

    dependencies = [
        ('mat_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_from_csv),
    ]
