from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

# from poker_app.accounts.models import UserModel

UserModel = get_user_model()


class Table(models.Model):
    MAX_PLAYERS = 5

    name = models.CharField(
        max_length=10
    )

    max_players = models.IntegerField(
        validators=(
            MaxValueValidator(MAX_PLAYERS),
        )
    )

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    #     # primary_key=True,
    # )

    # USERNAME_FIELD = 'username'
