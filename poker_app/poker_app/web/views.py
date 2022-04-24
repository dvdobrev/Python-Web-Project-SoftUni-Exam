from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.web.forms import CreateRoomForm, EditRoomForm, DeleteRoomForm

from poker_app.web.models import Room


class HomeView(views.TemplateView):
    template_name = 'home_page_no_profile.html'
    # template_name = 'index.html'
    # template_name = 'base.html'


class DashboardView(views.ListView):
    model = Room
    template_name = 'dashboard.html'
    # context_object_name = 'pet_photos'


class CreateRoomView(views.CreateView, auth_mixins.LoginRequiredMixin):
    template_name = 'games/../../templates/rooms/create-room.html'
    form_class = CreateRoomForm
    success_url = reverse_lazy('all rooms page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs['user_id'] = self.request.user.id
        return kwargs


class EditRoomView(views.UpdateView, auth_mixins.LoginRequiredMixin):
    model = Room
    template_name = 'games/../../templates/rooms/edit-room.html'
    form_class = EditRoomForm
    success_url = reverse_lazy('all rooms page')


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#
#     context['is_owner'] = self.object.user == self.request.user
#
#     return context


class DeleteRoomView(views.DeleteView):
    # def get_queryset(self):
    #     table = super().get_queryset().filter(table=self.request.id)
    #     return table

    model = Room
    template_name = 'games/../../templates/rooms/delete-room.html'
    form_class = DeleteRoomForm
    success_url = reverse_lazy('all rooms page')


def get_all_rooms(request):
    rooms = Room.objects.all()

    if not rooms:
        return redirect('create room page')

    context = {
        'rooms': rooms,
    }

    return render(request, 'rooms/all-rooms.html', context)
