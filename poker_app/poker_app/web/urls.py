from django.urls import path

from poker_app.web.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),

)
