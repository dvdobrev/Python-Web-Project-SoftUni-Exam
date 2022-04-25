# Generated by Django 4.0.4 on 2022-04-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('max_players', models.IntegerField()),
                ('min_bet', models.IntegerField()),
                ('max_bet', models.IntegerField()),
            ],
        ),
    ]