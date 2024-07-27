from rest_framework import serializers
from .models import CamDB

class CamDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamDB
        fields = '__all__'
