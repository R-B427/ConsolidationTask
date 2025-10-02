from django.contrib import admin
from .models import Event
from website.models import Album, Event, UserFavoriteAlbum

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue')
    search_fields = ('title', 'venue')
