from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from django.urls import reverse_lazy, reverse

from poker_app.accounts.forms import EditProfileForm, CreateProfileForm, DeleteProfileForm
from poker_app.accounts.models import Profile

from django.conf import settings
from django.core.mail import send_mail


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

    def user_log_in(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email)

            login(request, user)
            subject = 'Hi Dobri, I am trying to send an Email'
            message = f'So it works. Let drink a coffe Dobri'
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_form, recipient_list)

            return redirect('dashboard')
        return render(request, 'accounts/login-page.html')

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
