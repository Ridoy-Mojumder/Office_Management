from django.contrib import admin
from django.urls import path
from myProject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singupPage',singupPage,name="singupPage"),
    path('',singinPage,name="singinPage"),
    path('deshboardPage/',deshboardPage,name="deshboardPage"),
    path('logoutPage/',logoutPage,name="logoutPage"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

