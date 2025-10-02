from django.urls import path
from . import views

urlpatterns = [
    path('', views.echo_pulse_landing, name='landing'),  # public landing page
    path('home/', views.home, name='home_authenticated'),  # authenticated home page
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
