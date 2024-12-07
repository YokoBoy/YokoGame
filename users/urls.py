# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views
#
# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('support/', views.support, name='support'),
]
