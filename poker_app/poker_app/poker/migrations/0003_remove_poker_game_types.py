# Generated by Django 4.0.4 on 2022-04-25 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0002_remove_poker_max_players_remove_poker_min_bet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poker',
            name='game_types',
        ),
    ]