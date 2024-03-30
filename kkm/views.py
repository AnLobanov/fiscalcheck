from .models import KKM, ClientError
from rest_framework import generics
from .serializers import KKMSerializer, ErrorSerializer

class KKMAPIList(generics.CreateAPIView):
    queryset = KKM.objects.all()
    serializer_class = KKMSerializer

class KKMAPIRetrieve(generics.RetrieveUpdateAPIView):
    queryset = KKM.objects.all()
    serializer_class = KKMSerializer

class ErrorAPIList(generics.CreateAPIView):
    queryset = ClientError.objects.all()
    serializer_class = ErrorSerializer