"""URL Configuration for the EchoPulse Django application.

This module maps URL paths to their corresponding views.
Each route is associated with a named view, which can be referenced
through Django's URL reversing functions.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.echo_pulse_landing, name='landing'),
    path('home/', views.home, name='home_authenticated'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('albums/', views.albums, name='album_list'),
    path('artist/', views.artists, name='artists'),
    path('event/', views.events, name='events'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('album/<int:id>/', views.album_detail, name='album_detail'),
    path('event/<int:id>/', views.event_detail, name='event_detail'),
]