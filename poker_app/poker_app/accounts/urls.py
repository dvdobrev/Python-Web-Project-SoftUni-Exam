from django.urls import path

from poker_app.accounts.views import UserRegisterView, UserLoginView, EditProfileView, show_profile

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login page'),
    # path('profile/details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details page'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile page'),
    path('details/', show_profile, name='profile page'),

)
