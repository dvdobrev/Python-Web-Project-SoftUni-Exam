from django.shortcuts import render

from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.games.forms import CreateGameForm
from poker_app.games.models import GameType
from poker_app.web.forms import CreateRoomForm, EditRoomForm, DeleteRoomForm

from poker_app.web.models import Room


class CreateGameView(views.CreateView, auth_mixins.LoginRequiredMixin):
    template_name = 'games/create-game.html'
    form_class = CreateGameForm
    success_url = reverse_lazy('all rooms page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs['user_id'] = self.request.user.id
        return kwargs


def get_all_games(request):
    games = GameType.objects.all()

    if not games:
        return redirect('create game page')

    context = {
        'games': games,
    }

    return render(request, 'games/all-games.html', context)
