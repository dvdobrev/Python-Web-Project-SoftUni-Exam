from django.shortcuts import render

# Create your views here.
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.poker.forms import CreatePokerRoomForm, EditPokerRoomForm, DeletePokerRoomForm
from poker_app.poker.models import Poker


class CreatePokerRoomView(views.CreateView, auth_mixins.LoginRequiredMixin):
    template_name = 'rooms/poker_room/create-poker_room.html'
    form_class = CreatePokerRoomForm
    success_url = reverse_lazy('all rooms page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs['user_id'] = self.request.user.id
        return kwargs


class EditPokerRoomView(views.UpdateView, auth_mixins.LoginRequiredMixin):
    model = Poker
    template_name = 'rooms/poker_room/edit-poker-room.html'
    form_class = EditPokerRoomForm
    success_url = reverse_lazy('all rooms page')


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#
#     context['is_owner'] = self.object.user == self.request.user
#
#     return context


class DeletePokerRoomView(views.DeleteView):
    # def get_queryset(self):
    #     table = super().get_queryset().filter(table=self.request.id)
    #     return table

    model = Poker
    template_name = 'rooms/poker_room/delete-poker-room.html'
    form_class = DeletePokerRoomForm
    success_url = reverse_lazy('all rooms page')


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
#     return render(request, 'rooms/all-rooms.html', context)
