from django.urls import path

from poker_app.roulette.views import CreateRouletteGameView, EditRouletteGameView, DeleteRouletteGameView

urlpatterns = (

    path('create/', CreateRouletteGameView.as_view(), name='create roulette game page'),
    path('edit/<int:pk>/', EditRouletteGameView.as_view(), name='edit roulette game page'),
    path('delete/<int:pk>/', DeleteRouletteGameView.as_view(), name='delete roulette game page'),

)
