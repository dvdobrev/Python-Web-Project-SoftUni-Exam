from django.urls import path

from poker_app.dice.views import CreateDiceRoomView, EditDiceRoomView, DeleteDiceRoomView

urlpatterns = (

    path('create/', CreateDiceRoomView.as_view(), name='create dice game page'),
    path('edit/<int:pk>/', EditDiceRoomView.as_view(), name='edit dice game page'),
    path('delete/<int:pk>/', DeleteDiceRoomView.as_view(), name='delete dice game page'),

)
