from django.urls import path

from poker_app.accounts.views import UserRegisterView, UserLoginView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('profile/', UserLoginView.as_view(), name='profile page'),

    # path('profile/', it_works, name='it works'),

)
