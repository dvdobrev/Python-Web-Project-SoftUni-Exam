from django.test import TestCase
from django.urls import reverse

from poker_app.poker.models import Poker


class CreatePokerGameViewTests(TestCase):
    POKER_GAME_DATA = {
        'name': 'p1',
        # 'max_players': 5,
        # 'min_bet': 5,
        # 'max_bet': 5,

    }

    def test_check_if_game_is_created(self):
        self.client.post(
            reverse('create poker game page'),
            data=self.POKER_GAME_DATA,
        )

        poker = Poker.objects.first()
        pass
