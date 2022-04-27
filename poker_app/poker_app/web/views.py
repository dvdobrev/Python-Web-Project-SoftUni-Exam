from django.shortcuts import redirect, render
from django.views import generic as views

from poker_app.dice.models import Dice
from poker_app.poker.models import Poker
from poker_app.roulette.models import Roulette


class HomeView(views.TemplateView):
    template_name = 'home_page_no_profile.html'

class DashboardView(views.ListView):
    model = Poker
    template_name = 'dashboard.html'


def get_all_games(request):
    ERROR_MESSAGE = 'There is no GAMES. You have to create a game'

    poker_games = Poker.objects.all()
    dice_games = Dice.objects.all()
    roulette_games = Roulette.objects.all()

    if not poker_games and not dice_games and not roulette_games:
        # TODO: 'Write error message'
        # TODO: 'You can make a signal here: for the error message'
        return redirect('dashboard')

    context = {
        'poker_games': poker_games,
        'dice_games': dice_games,
        'roulette_games': roulette_games,
    }

    return render(request, 'games/all-games.html', context)
