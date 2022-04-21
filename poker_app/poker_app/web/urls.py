from django.urls import path

from poker_app.web.views import HomeView, CreateTableView, get_all_tables, DashboardView, EditTableView

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


    path('table/create/', CreateTableView.as_view(), name='create table page'),
    path('table/edit/<int:pk>/', EditTableView.as_view(), name='edit table page'),
    path('table/all-tables/', get_all_tables, name='all tables page'),

)
