from django.contrib import admin
from .models import Event
from website.models import Album, Event, UserFavoriteAlbum

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Event model.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields searchable in the admin search bar.
    """
    list_display = ('title', 'date', 'venue')
    search_fields = ('title', 'venue')
