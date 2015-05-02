from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers


from .models import FAQApp, AboutUs


def faq_api(request):
    data = serializers.serialize('json',
        FAQApp.objects.all(),
        fields = ('question', 'answer')
        )
    return HttpResponse(data)


def about_api(request):
    data = serializers.serialize('json',
        AboutUs.objects.all(),
        fields='about_us')
    return HttpResponse(data)


    

