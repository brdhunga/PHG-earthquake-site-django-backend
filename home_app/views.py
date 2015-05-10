from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import WhyUs
from home_app.serializer import HomeSerializer


def home(request):
    b = HttpResponse("<h1>This is great</h1>")
    print(dir(b))
    return HttpResponse("<h1>This is great</h1>") 


@api_view(['GET'])
def home_api(request):
    if request.method == 'GET':
        why_us = WhyUs.objects.all()
        serializer = HomeSerializer(why_us, many=True)
        return Response(serializer.data)






