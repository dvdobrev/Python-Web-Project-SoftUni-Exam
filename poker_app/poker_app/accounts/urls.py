from django.conf import settings
from django.contrib.auth import logout
from django.urls import path, include


from poker_app.accounts.views import UserRegisterView, UserLoginView, ProfileEditView, ProfileDetailsView, \
    UserLogoutView, delete_profile

urlpatterns = (
    # path('accounts/', include('django.contrib.auth.urls')),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('logout/', UserLogoutView.as_view(), name='logout page'),


    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout page'),


    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details page'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit profile page'),

    # path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete page'),
    path('delete/<int:pk>/', delete_profile, name='profile delete page'),

)
