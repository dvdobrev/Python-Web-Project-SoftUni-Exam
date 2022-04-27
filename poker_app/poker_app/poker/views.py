from django.contrib.auth import mixins as auth_mixins, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.poker.forms import CreatePokerGameForm, EditPokerGameForm, DeletePokerGameForm
from poker_app.poker.models import Poker


class CreatePokerGameView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'games/poker_room/create-poker-game.html'
    form_class = CreatePokerGameForm
    success_url = reverse_lazy('all games page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPokerGameView(views.UpdateView, auth_mixins.LoginRequiredMixin):
    model = Poker
    template_name = 'games/poker_room/edit-poker-game.html'

    form_class = EditPokerGameForm
    success_url = reverse_lazy('all games page')


def edit_poker_game(request, pk):
    poker = Poker.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPokerGameForm(request.POST, instance=poker)
        if form.is_valid():
            form.save()
            return redirect('all games page')

    else:
        form = EditPokerGameForm(instance=poker)

    context = {
        'form': form,
        'poker': poker,
    }

    return render(request, 'games/poker_room/edit-poker-game.html', context)


class DeletePokerGameView(views.DeleteView):
    model = Poker
    template_name = 'games/poker_room/delete-poker-game.html'
    form_class = DeletePokerGameForm
    success_url = reverse_lazy('all games page')
