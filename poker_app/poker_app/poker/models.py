from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

UserModel = get_user_model()
from poker_app.accounts.models import PokerUser


class Poker(models.Model):
    # TEXAS_HOLEM = 'Texas Holdem'
    # OMAHA = 'Omaha'
    #
    # GAME_TYPES = [(x, x) for x in (TEXAS_HOLEM, OMAHA)]

    name = models.CharField(
        max_length=10
    )

    # max_players = models.IntegerField()
    #
    # min_bet = models.IntegerField()
    # max_bet = models.IntegerField()
    #
    # user = models.OneToOneField(
    #     UserModel,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    user = models.ForeignKey(
        UserModel,
        on_delete=CASCADE
    )

    # game_types = models.CharField(
    #     max_length=max(len(x) for x, _ in GAME_TYPES),
    #     choices=GAME_TYPES,
    #     null=True,
    #     blank=True,
    # )
