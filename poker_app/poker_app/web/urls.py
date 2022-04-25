from django.urls import path

from poker_app.web.views import HomeView, DashboardView, get_all_rooms

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # path('dice/create/', CreateDiceRoomView.as_view(), name='create dice room page'),
    # path('dice/edit/<int:pk>/', EditDiceRoomView.as_view(), name='edit dice room page'),
    # path('dice/delete/<int:pk>/', DeleteDiceRoomView.as_view(), name='delete dice room page'),
    # # path('table/delete/<int:pk>/', DeleteRoomView.as_view(), name='delete table page'),

    path('all-rooms/', get_all_rooms, name='all rooms page'),

    # path('poker/create/', CreatePokerRoomView.as_view(), name='create poker room page'),
    # path('poker/edit/<int:pk>/', EditPokerRoomView.as_view(), name='edit poker room page'),
    # path('poker/delete/<int:pk>/', DeletePokerRoomView.as_view(), name='delete poker room page'),

#     path('roulette/create/', CreateRouletteRoomView.as_view(), name='create roulette room page'),
#     path('roulette/edit/<int:pk>/', EditRouletteRoomView.as_view(), name='edit roulette room page'),
#     path('roulette/delete/<int:pk>/', DeleteRouletteRoomView.as_view(), name='delete roulette room page'),

)
