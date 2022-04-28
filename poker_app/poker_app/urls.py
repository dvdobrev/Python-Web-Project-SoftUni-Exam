from django.contrib import admin
from django.urls import path, include

urlpatterns = [
          path('admin/', admin.site.urls),
          path('', include('poker_app.web.urls')),
          path('accounts/', include('poker_app.accounts.urls')),
          path('roulette/', include('poker_app.roulette.urls')),
          path('dice/', include('poker_app.dice.urls')),
          path('poker/', include('poker_app.poker.urls')),
    ]
      # ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
