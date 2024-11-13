from django.shortcuts import render
from API_IOT.models import IOT
from API_IOT.serializer import IOTSerializer
from django.http import JsonResponse



def list(request):
    Iot = IOT.objects.all()
    serial = IOTSerializer(Iot, many=True)
    return JsonResponse(serial.data, safe=False)  
# Create your views here.  