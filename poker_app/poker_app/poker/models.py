from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from poker_app.web.validators import validate_only_letters, GameMaxPlayersValidator, GameMinPlayersValidator

UserModel = get_user_model()
from poker_app.accounts.models import PokerUser


# @login_required(UserModel)
class Poker(models.Model):
    GAME_MAX_PLAYERS = 10
    GAME_MIN_PLAYERS = 2

    NAME_MAX_LENGTH = 10


    # TEXAS_HOLEM = 'Texas Holdem'
    # OMAHA = 'Omaha'
    #
    # GAME_TYPES = [(x, x) for x in (TEXAS_HOLEM, OMAHA)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validate_only_letters,
        ),
        unique=True,
    )

    max_players = models.IntegerField(
        validators=(
            GameMaxPlayersValidator(GAME_MAX_PLAYERS),
            # GameMinPlayersValidator(GAME_MIN_PLAYERS),
        )
    )
    # min_bet = models.IntegerField()
    # max_bet = models.IntegerField()

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
