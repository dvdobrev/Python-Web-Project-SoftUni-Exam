from django.urls import path

from poker_app.web.views import HomeView, DashboardView, get_all_games

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('all-games/', get_all_games, name='all games page'),

)
