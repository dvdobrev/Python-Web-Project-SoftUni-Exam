from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('poker_app.web.urls')),
    path('accounts/', include('poker_app.accounts.urls')),
    path('games/', include('poker_app.games.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
