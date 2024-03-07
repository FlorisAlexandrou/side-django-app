from mat_app.models import Client
from mat_app.serializers import ClientSerializer
from rest_framework import generics
from rest_framework import filters


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'address']
    ordering_fields = '__all__'


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
