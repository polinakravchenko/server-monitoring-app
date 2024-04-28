from rest_framework import serializers
from .models import Servers

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servers
        fields = '__all__'
