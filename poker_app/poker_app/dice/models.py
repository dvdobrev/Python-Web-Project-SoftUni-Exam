from django.db import models


# UserModel = get_user_model()


class Dice(models.Model):

    name = models.CharField(
        max_length=10
    )

    # max_players = models.IntegerField()
    #
    # min_bet = models.IntegerField()
    # max_bet = models.IntegerField()

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    #     # primary_key=True,
    # )
    #
    # game_types = models.CharField(
    #     max_length=max(len(x) for x, _ in GAME_TYPES),
    #     choices=GAME_TYPES,
    #     null=True,
    #     blank=True,
    # )
