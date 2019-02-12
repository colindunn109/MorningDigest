from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from .views import HomePage
from news.views import techScrape

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage.as_view(),name="homepage"),
    path('news/',include("news.urls" , namespace="news")),
    path('techScrape/',techScrape,name="techScrape")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
