# Generated by Django 3.2.23 on 2024-04-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_v2', '0017_honeytrees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honeytrees',
            name='rarity',
            field=models.CharField(max_length=30),
        ),
    ]
