
from django.contrib.auth import mixins as auth_mixins, login

from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.poker.forms import CreatePokerGameForm, EditPokerGameForm, DeletePokerGameForm
from poker_app.poker.models import Poker


class CreatePokerGameView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'games/poker_room/create-poker_game.html'
    form_class = CreatePokerGameForm
    success_url = reverse_lazy('all games page')
    # context_object_name = 'poker'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs['user_id'] = self.request.user.id
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # context['is_owner'] = self.object.user == self.request.user
    #
    #     return context
    #
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     # user => self.object
    #     # request => self.request
    #     login(self.request, self.object)
    #     return result


class EditPokerGameView(views.UpdateView, auth_mixins.LoginRequiredMixin):
    model = Poker
    template_name = 'games/poker_room/edit-poker-game.html'
    # context_object_name = 'poker'

    form_class = EditPokerGameForm
    success_url = reverse_lazy('all games page')


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#
#     context['is_owner'] = self.object.user == self.request.user
#
#     return context


class DeletePokerGameView(views.DeleteView):
    # def get_queryset(self):
    #     table = super().get_queryset().filter(table=self.request.id)
    #     return table

    model = Poker
    template_name = 'games/poker_room/delete-poker-game.html'
    form_class = DeletePokerGameForm
    success_url = reverse_lazy('all games page')

# def get_all_rooms(request):
#     poker_games = Poker.objects.all()
#
#     if not poker_games:
#         return redirect('create poker page')
#
#     context = {
#         'poker_games': poker_games,
#     }
#
#     return render(request, 'games/all-games.html', context)
