from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.dice.forms import CreateDiceRoomForm, EditDiceRoomForm, DeleteDiceRoomForm
from poker_app.dice.models import Dice


class CreateDiceRoomView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'games/dice_room/create-dice_game.html'
    form_class = CreateDiceRoomForm
    success_url = reverse_lazy('all games page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditDiceRoomView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Dice
    template_name = 'games/dice_room/edit-dice-game.html'
    form_class = EditDiceRoomForm
    success_url = reverse_lazy('all games page')


class DeleteDiceRoomView(views.DeleteView):
    model = Dice
    template_name = 'games/dice_room/delete-dice-game.html'
    form_class = DeleteDiceRoomForm
    success_url = reverse_lazy('all games page')
