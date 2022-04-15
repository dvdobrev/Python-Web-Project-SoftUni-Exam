
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('poker_app.web.urls')),
    path('accounts/', include('poker_app.accounts.urls')),
]
