from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from django.urls import reverse_lazy

from poker_app.accounts.forms import EditProfileForm, CreateProfileForm, DeleteProfileForm
from poker_app.accounts.models import Profile, PokerUser


# TODO: 'add RedirectToHomePage to the UserRegisterView'


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        # user => self.object
        # request = self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    # template_name = 'accounts/logout-page.html'
    # success_url = reverse_lazy('home page')
    pass


class ProfileEditView(views.UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('dashboard')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'
    success_url = reverse_lazy('home page')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # self.object is a Profile instance
    #     tables = list(Poker.objects.filter(user_id=self.object.user_id))
    #
    #     context.update({
    #         # 'total_likes_count': total_likes_count,
    #         # 'total_pet_photos_count': total_pet_photos_count,
    #         'is_owner': self.object.user_id == self.request.user.id,
    #         'tables': tables,
    #     })
    #
    #     return context


@login_required
def delete_profile(request, pk):
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        # messages.info(request, 'Your account has been deleted.')
        return redirect('home page')
    else:
        form = DeleteProfileForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/profile-delete.html', context)

#
# class ChangeUserPasswordView(auth_views.PasswordChangeView):
#     template_name = 'accounts/change_password.html'
