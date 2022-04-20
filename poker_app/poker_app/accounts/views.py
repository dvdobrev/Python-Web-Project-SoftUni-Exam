from django.views import generic as views
from django.contrib.auth import views as auth_views

# Create your views here.
from django.urls import reverse_lazy

from poker_app.accounts.forms import EditProfileForm
from poker_app.web.forms import CreateProfileForm
from poker_app.web.views_mixin import RedirectToHomePage


# TODO: 'add RedirectToHomePage to the UserRegisterView'

class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm
