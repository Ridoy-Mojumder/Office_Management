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
    path('profilePage/',profilePage,name="profilePage"),
    path('add_taskPage/',add_taskPage,name="add_taskPage"),
    path('view_taskPage/',view_taskPage,name="view_taskPage"),
    path('view_team_member_page/',view_team_member_page,name="view_team_member_page"),
    path('delete_taskPage/<str:myid>',delete_taskPage,name="delete_taskPage"),
    path('edit_taskPage/<str:myid>',edit_taskPage,name="edit_taskPage"),
    path('update_taskPage',update_taskPage,name="update_taskPage"),
    path('message_Page',message_Page,name="message_Page"),
    path('contactUs_Page',contactUs_Page,name="contactUs_Page"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

