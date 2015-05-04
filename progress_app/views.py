from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


from .models import Progress


def progress_api(request):
    data = serializers.serialize('json',
        Progress.objects.all(),
        fields=('title', 'slug', 'summary', 'content', 'created_at')
        )
    return HttpResponse(data) 



def progress_single_api(request, slug):
    data = serializers.serialize('json',
        Progress.objects.filter(slug=slug),
        fields=('title', 'slug', 'summary', 'content', 'created_at')
        )
    return HttpResponse(data) 



