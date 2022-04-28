from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from poker_app.web.validators import RouletteMinPlayersValidator, MinBetValidator, MaxBetValidator

UserModel = get_user_model()


class Roulette(models.Model):
    GAME_MAX_PLAYERS = 20
    GAME_MIN_PLAYERS = 1

    GAME_MAX_BET = 50
    GAME_MIN_BET = 5

    # EUROPEAN = 'European'
    # AMERICAN = 'American'
    #
    # GAME_TYPES = [(x, x) for x in (EUROPEAN, AMERICAN)]

    name = models.CharField(
        max_length=10,
        unique=True,

    )

    max_players = models.IntegerField(
        validators=(
            MaxValueValidator(GAME_MAX_PLAYERS),
            RouletteMinPlayersValidator(GAME_MAX_PLAYERS)
        )
    )

    min_bet = models.IntegerField(
        validators=(
            MinBetValidator(GAME_MIN_BET),
        )
    )

    max_bet = models.IntegerField(
        validators=(
            MaxBetValidator(GAME_MAX_BET),
        )
    )

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
