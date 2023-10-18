from rest_framework import serializers
from .models import KKM

class KKMSerializer(serializers.ModelSerializer):
    class Meta:
        model = KKM
        fields = ('__all__')