from django.urls import path, include


from poker_app.accounts.views import UserRegisterView, UserLoginView, ProfileEditView, ProfileDetailsView, \
    ProfileDeleteView

urlpatterns = (
    # path('accounts/', include('django.contrib.auth.urls')),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details page'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit profile page'),

    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete page'),
    # path('delete/<int:pk>/', delete_profile, name='profile delete page'),

)
