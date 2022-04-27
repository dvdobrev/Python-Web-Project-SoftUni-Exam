from django.urls import path

from poker_app.poker.views import EditPokerGameView, DeletePokerGameView, \
    CreatePokerGameView

urlpatterns = (

    path('create/', CreatePokerGameView.as_view(), name='create poker game page'),
    # path('create/', create_poker_game, name='create poker game page'),

    path('edit/<int:pk>/', EditPokerGameView.as_view(), name='edit poker game page'),
    # path('edit/<int:pk>/', edit_poker_game, name='edit poker game page'),


    path('delete/<int:pk>/', DeletePokerGameView.as_view(), name='delete poker game page'),

)
