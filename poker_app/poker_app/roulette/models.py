from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Roulette(models.Model):
    # EUROPEAN = 'European'
    # AMERICAN = 'American'
    #
    # GAME_TYPES = [(x, x) for x in (EUROPEAN, AMERICAN)]

    name = models.CharField(
        max_length=10
    )

    # max_players = models.IntegerField()
    #
    # min_bet = models.IntegerField()
    # max_bet = models.IntegerField()

    #
    # game_types = models.CharField(
    #     max_length=max(len(x) for x, _ in GAME_TYPES),
    #     choices=GAME_TYPES,
    #     null=True,
    #     blank=True,
    # )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
