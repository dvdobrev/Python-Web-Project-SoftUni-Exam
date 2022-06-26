from poker_app.web.signals import *
from django.urls import path


from poker_app.accounts.views import UserRegisterView, ProfileEditView, ProfileDetailsView, \
    UserLogoutView, delete_profile, UserLoginView, ChangeUserPasswordView

urlpatterns = (

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login page'),
    # path('login/', user_log_in, name='login page'),
    path('logout/', UserLogoutView.as_view(), name='logout page'),


    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details page'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit profile page'),
    path('change-password/', ChangeUserPasswordView.as_view(), name='change password'),

    # path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete page'),
    path('delete/<int:pk>/', delete_profile, name='profile delete page'),

)


