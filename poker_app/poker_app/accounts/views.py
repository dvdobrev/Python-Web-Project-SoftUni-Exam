from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from poker_app.web.forms import CreateProfileForm
from poker_app.web.models import Table
from poker_app.web.views_mixin import RedirectToHomePage


class UserRegisterView(RedirectToHomePage, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'register.html'
    success_url = reverse_lazy('home page')


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class DashboardView(views.ListView):
    model = Table
    template_name = 'dashboard.html'
    # context_object_name = 'pet_photos'
