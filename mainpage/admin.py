from django.contrib import admin

from mainpage.models import Event_item

@admin.register(Event_item)
class Event_itemAdmin(admin.ModelAdmin):
    model = Event_item

    list_display = ('title', 'event_date', 'price')
