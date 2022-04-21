from django.urls import path, include

from poker_app.accounts.forms import EditProfileForm
from poker_app.accounts.views import UserRegisterView, UserLoginView, EditProfileView, ProfileDetailsView

urlpatterns = (
    # path('accounts/', include('django.contrib.auth.urls')),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details page'),
    path('edit/<int:pk>/', EditProfileForm, name='edit profile page'),
    # path('delete/', DeleteProfileForm, name='profile delete page'),

)
