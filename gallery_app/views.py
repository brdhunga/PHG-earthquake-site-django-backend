import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Event


def event_api(request):
    data = serializers.serialize('json',
        Event.objects.all(),
        fields = ('name', 'cover_image', 'slug', 'description')
        )
    return HttpResponse(data)


def event_single_api(request, slug):
    events = Event.objects.filter(slug=slug)
    data = serializers.serialize('json',
        events,
        fields=('name', 'cover_image', 'slug', 'description')
        )
    event = events[0]
    event_name = event.name.name
    images = event.images.all()
    images_data = serializers.serialize('json',
        images,
        fields=('url', 'caption', 'created_at')
        )
    data_dict = json.loads(data)[0]
    images_data_dict = json.loads(images_data)
    data_dict['images'] = images_data_dict
    data_dict['name'] = event_name
    return JsonResponse(data_dict)


