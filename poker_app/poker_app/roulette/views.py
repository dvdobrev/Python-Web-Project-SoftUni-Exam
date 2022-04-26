from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.roulette.forms import CreateRouletteRoomForm, EditRouletteRoomForm, DeleteRouletteRoomForm
from poker_app.roulette.models import Roulette


class CreateRouletteGameView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'games/roulette_room/create-roulette-game.html'
    form_class = CreateRouletteRoomForm
    success_url = reverse_lazy('all games page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs['user_id'] = self.request.user.id
        return kwargs


class EditRouletteGameView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Roulette
    template_name = 'games/roulette_room/edit-roulette-game.html'
    form_class = EditRouletteRoomForm
    success_url = reverse_lazy('all games page')


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#
#     context['is_owner'] = self.object.user == self.request.user
#
#     return context


class DeleteRouletteGameView(views.DeleteView):
    # def get_queryset(self):
    #     table = super().get_queryset().filter(table=self.request.id)
    #     return table

    model = Roulette
    template_name = 'games/roulette_room/delete-roulette-game.html'
    form_class = DeleteRouletteRoomForm
    success_url = reverse_lazy('all games page')

# def get_all_rooms(request):
#     roulette_games = Roulette.objects.all()
#
#     if not roulette_games:
#         return redirect('create roulette room page')
#
#     context = {
#         'roulette_games': roulette_games,
#     }
#
#     return render(request, 'games/all-games.html', context)
