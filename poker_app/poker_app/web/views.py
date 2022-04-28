from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import Http404
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

    def user_log_in(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email)

            login(request, user)
            subject = 'Hi Dobri, I am trying to send an Email'
            message = f'So it works. Let drink a coffe Dobri'
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_form, recipient_list)

            return redirect('dashboard')
        return render(request, 'accounts/login-page.html')


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


class Exceptions(Exception):
    pass


def raises_exception():
    # raise Http404('Dobri throw exception')
    raise Exceptions('Dobri throw exception')
