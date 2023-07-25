from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from edirektoriapjiiapps.models import *
from edirektoriapjiiapps.pagination import CustomPagination
from edirektoriapjiiapps.serializers import *
from rest_framework.authtoken.models import Token

class MasterKategoriView(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = MasterKategori.objects.all().order_by("-pk")
    serializer_class = MasterKategoriSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ("nama")

class ArtikelView(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Artikel.objects.all().order_by("-pk")
    serializer_class = ArtikelSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ("nama")