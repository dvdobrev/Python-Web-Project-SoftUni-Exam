from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from poker_app.accounts.forms import CreateProfileForm
from poker_app.web.views_mixin import RedirectToHomePage


class UserRegisterView(views.CreateView):  # RedirectToHomePage,
    form_class = CreateProfileForm
    template_name = 'register.html'
    success_url = reverse_lazy('home page')


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('it works')
    #
    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #     return super().get_success_url()


def it_works(request):
    return render(request,'profile.html')

