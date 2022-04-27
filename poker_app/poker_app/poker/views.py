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

    # context_object_name = 'poker'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['owner_id'] = self.request.user
    #
    #     return context

    #
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs['ownerrr_id'] = self.request.user.id
        return kwargs


# @login_required
# def create_poker_game(request, user=None, owner_id=None):
#     if request.method == 'POST':
#
#         user = request.user
#         owner_id = user.id
#         form = CreatePokerGameForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('all games page')
#         # form = CreatePokerGameForm(request.POST)
#         # user = request.user
#         # owner_id = request.user.id
#         # messages.info(request, 'Your account has been deleted.')
#     else:
#         form = CreatePokerGameForm(user)
#
#     context = {
#         'form': form,
#         'owner_id': owner_id,
#
#     }
#
#     return render(request, 'games/poker_room/create-poker-game.html', context)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
    #
    # def form_valid(self, form):
    #
    #     result = super().form_valid(form)
    #     # user => self.object
    #     # request => self.request
    #     return result

    # def form_valid(self, form):
    #     form.instance.owneeer_id = self.request.user.id
    #     return super().form_valid(form)


#
class EditPokerGameView(views.UpdateView, auth_mixins.LoginRequiredMixin):
    model = Poker
    template_name = 'games/poker_room/edit-poker-game.html'
    # context_object_name = 'poker'

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
