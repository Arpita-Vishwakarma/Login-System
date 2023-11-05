from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('Login/', views.Login, name='Login'),
    path('ragi/', views.ragi, name='ragi'),
    path('/logout', views.logout, name='logout'),
]
