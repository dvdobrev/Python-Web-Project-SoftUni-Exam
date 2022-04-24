# Generated by Django 4.0.4 on 2022-04-24 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type', models.CharField(blank=True, choices=[('Texas Holdem', 'Texas Holdem'), ('Omaha', 'Omaha')], max_length=12, null=True)),
                ('start_bet', models.IntegerField()),
                ('min_step_bet', models.IntegerField()),
                ('max_bet', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.room')),
            ],
        ),
    ]
