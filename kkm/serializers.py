from rest_framework import serializers
from .models import KKM, ClientError

class KKMSerializer(serializers.ModelSerializer):
    class Meta:
        model = KKM
        fields = ('__all__')

class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientError
        fields = ('__all__')