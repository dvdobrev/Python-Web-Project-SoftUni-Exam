from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

# Create your views here.
from django.urls import reverse_lazy

from poker_app.accounts.forms import EditProfileForm, CreateProfileForm
from poker_app.accounts.models import Profile
from poker_app.web.models import Table
from poker_app.web.views_mixin import RedirectToHomePage


# TODO: 'add RedirectToHomePage to the UserRegisterView'

class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        # user => self.object
        # request = self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    template_name = 'accounts/profile-edit.html'
    form_class = EditProfileForm


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        tables = list(Table.objects.filter(id=self.object.user_id))
        #
        #     # pet_photos = PetPhoto.objects \
        #     #     .filter(tagged_pets__in=pets) \
        #     #     .distinct()
        #
        #     # total_likes_count = sum(pp.likes for pp in pet_photos)
        #     # total_pet_photos_count = len(pet_photos)
        #
        #     context.update({
        #         # 'total_likes_count': total_likes_count,
        #         # 'total_pet_photos_count': total_pet_photos_count,
        #         'is_owner': self.object.user_id == self.request.user.id,
        #         'tables': tables,
        #     })
        #
        return context

# def show_profile(request):
#     profile = Profile.objects.all()[0]
#
#     context = {
#         'profile': profile,
#     }
#     return render(request, 'accounts/profile-details.html', context)
