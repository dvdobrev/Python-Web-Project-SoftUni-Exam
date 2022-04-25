from django.urls import path

from poker_app.poker.views import CreatePokerRoomView, EditPokerRoomView, DeletePokerRoomView

urlpatterns = (

    path('create/', CreatePokerRoomView.as_view(), name='create poker game page'),
    path('edit/<int:pk>/', EditPokerRoomView.as_view(), name='edit poker game page'),
    path('delete/<int:pk>/', DeletePokerRoomView.as_view(), name='delete poker game page'),

)
