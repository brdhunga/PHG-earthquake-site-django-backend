from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


from .models import WhyUs


def home(request):
    return HttpResponse("<h1>This is great</h1>") 


def home_api(request):
    data = serializers.serialize('json',
        WhyUs.objects.all(),
        fields=('why_us')
        )
    return HttpResponse(data) 





