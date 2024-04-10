# Generated by Django 3.2.23 on 2024-04-10 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_v2', '0016_machinelocations'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoneyTrees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity', models.CharField(max_length=30)),
                ('pokemon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='honeytrees', to='pokemon_v2.pokemon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
