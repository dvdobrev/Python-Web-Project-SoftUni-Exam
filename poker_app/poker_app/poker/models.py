from django.contrib.auth import get_user_model
from django.db import models

from poker_app.web.validators import validate_only_letters, GameMaxPlayersValidator, GameMinPlayersValidator, \
    MinBetValidator, MaxBetValidator

UserModel = get_user_model()
from poker_app.accounts.models import PokerUser


class Poker(models.Model):
    NAME_MAX_LENGTH = 30

    GAME_MAX_PLAYERS = 5
    GAME_MIN_PLAYERS = 2

    GAME_MAX_BET = 200
    GAME_MIN_BET = 2

    TEXAS_HOLEM = 'Texas Holdem'
    OMAHA = 'Omaha'
    OMAHA2 = 'Omaha2'
    DO_NOT_SHOW = 'Do not show'

    # GAME_TYPES = [(x, x) for x in (TEXAS_HOLEM, OMAHA, OMAHA2)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=(
            validate_only_letters,
        ),
    )

    max_players = models.IntegerField(
        validators=(
            GameMaxPlayersValidator(GAME_MAX_PLAYERS),
            GameMinPlayersValidator(GAME_MIN_PLAYERS),
        ),
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

    # game_types = models.CharField(
    #     max_length=max(len(x) for x, _ in GAME_TYPES),
    #     choices=GAME_TYPES,
    #     null=True,
    #     blank=True,
    #     default=DO_NOT_SHOW,
    #
    # )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
