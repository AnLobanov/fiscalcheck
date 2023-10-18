from django.shortcuts import render
from .models import KKM
from rest_framework import generics
from .serializers import KKMSerializer

class KKMAPIView(generics.ListAPIView):
    queryset = KKM.objects.all()
    serializer_class=KKMSerializer
