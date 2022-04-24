from django.urls import path

from poker_app.games.views import CreateGameView
from poker_app.web.views import HomeView, CreateRoomView, get_all_rooms, DashboardView, EditRoomView, DeleteRoomView

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('room/create/', CreateRoomView.as_view(), name='create room page'),
    path('room/edit/<int:pk>/', EditRoomView.as_view(), name='edit room page'),
    path('room/delete/<int:pk>/', DeleteRoomView.as_view(), name='delete room page'),
    # path('table/delete/<int:pk>/', DeleteRoomView.as_view(), name='delete table page'),

    path('room/all-rooms/', get_all_rooms, name='all rooms page'),


)
