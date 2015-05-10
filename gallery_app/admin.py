from django.contrib import admin

from .models import Image, Event, EventName


admin.site.register(EventName)
admin.site.register(Image)
admin.site.register(Event)



