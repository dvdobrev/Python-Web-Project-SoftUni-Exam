from django.urls import path

from poker_app.accounts.views import UserRegisterView, UserLoginView, EditProfileView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('profile/', UserLoginView.as_view(), name='profile page'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile page'),



)
