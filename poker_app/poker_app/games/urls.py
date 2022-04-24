from django.urls import path

from poker_app.games.views import CreateGameView, get_all_games

urlpatterns = (
    path('create/', CreateGameView.as_view(), name='create game page'),
    path('all-games/', get_all_games, name='all games page'),
)
