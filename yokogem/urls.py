from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from lessons.views import page_not_found

from users.views import mainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage, name='mainPage'),
    path('lessons/', include('lessons.urls')),  # Маршруты для lessons
    path('users/', include('users.urls')),  # Маршруты для users
]

handler404 = page_not_found