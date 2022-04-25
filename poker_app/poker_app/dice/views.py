from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.dice.forms import CreateDiceRoomForm, EditDiceRoomForm, DeleteDiceRoomForm
from poker_app.dice.models import Dice


class CreateDiceRoomView(views.CreateView, auth_mixins.LoginRequiredMixin):
    template_name = 'rooms/dice_room/create-dice_room.html'
    form_class = CreateDiceRoomForm
    success_url = reverse_lazy('all rooms page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs['user_id'] = self.request.user.id
        return kwargs


class EditDiceRoomView(views.UpdateView, auth_mixins.LoginRequiredMixin):
    model = Dice
    template_name = 'rooms/dice_room/edit-dice-room.html'
    form_class = EditDiceRoomForm
    success_url = reverse_lazy('all rooms page')


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#
#     context['is_owner'] = self.object.user == self.request.user
#
#     return context


class DeleteDiceRoomView(views.DeleteView):
    # def get_queryset(self):
    #     table = super().get_queryset().filter(table=self.request.id)
    #     return table

    model = Dice
    template_name = 'rooms/dice_room/delete-dice-room.html'
    form_class = DeleteDiceRoomForm
    success_url = reverse_lazy('all rooms page')


# def get_all_rooms(request):
#     dice = Dice.objects.all()
#
#     if not dice:
#         return redirect('create dice room page')
#
#     context = {
#         'dice': dice,
#     }
#
#     return render(request, 'rooms/all-rooms.html', context)
