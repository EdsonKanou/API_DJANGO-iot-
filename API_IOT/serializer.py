from rest_framework import serializers
from API_IOT.models import IOT 

class IOTSerializer(serializers.ModelSerializer):
    class Meta:
        model:IOT 
        fields=['id','postion','status']
