from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group
import json

class MasterKategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterKategori
        fields = "__all__"

class ArtikelSerializer(serializers.ModelSerializer):
    kategori = MasterKategoriSerializer()
    class Meta:
        model = Artikel
        fields = "__all__"