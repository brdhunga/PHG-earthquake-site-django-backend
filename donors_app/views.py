from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


from .models import Donors


def donors_api(request):
    data = serializers.serialize('json',
        Donors.objects.all(),
        fields = ('name', 'contribution')
        )
    return HttpResponse(data)





