from django.urls import path

from poker_app.roulette.views import CreateRouletteRoomView, EditRouletteRoomView, DeleteRouletteRoomView

urlpatterns = (

    path('create/', CreateRouletteRoomView.as_view(), name='create roulette game page'),
    path('edit/<int:pk>/', EditRouletteRoomView.as_view(), name='edit roulette game page'),
    path('delete/<int:pk>/', DeleteRouletteRoomView.as_view(), name='delete roulette game page'),

)
