from django.contrib.auth import get_user_model
from django.db import models

from poker_app.web.models import Room

# UserModel = get_user_model()


class GameType(models.Model):
    TEXAS_HOLEM = 'Texas Holdem'
    OMAHA = 'Omaha'

    GAME_TYPES = [(x, x) for x in (TEXAS_HOLEM, OMAHA)]

    game_type = models.CharField(
        max_length=max(len(x) for x, _ in GAME_TYPES),
        choices=GAME_TYPES,
        null=True,
        blank=True,
        # default=DO_NOT_SHOW,
    )

    # game_type_in_room = models.ManyToManyField(
    #     Room,
    # )
    #
    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )
