from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from edirektoriapjiiapps.models import *
from edirektoriapjiiapps.serializers import *
# from edirektoriapjiiapps.index import image_check
# from django.core.files.storage import default_storage
import json

# Master Kategori
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getKategori(request):
    item = MasterKategori.objects.all().order_by("nama")
    serializer = MasterKategoriSerializer(
        item, context={"request": request}, many=True
    )
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def createKategori(request):
    data = request.data

    create = MasterKategori.objects.create(
        nama=data["nama"],
    )
    create.save()
    return Response({"status": 200, "messages": "Data Berhasil Ditambah!"})

@api_view(["PUT", "DELETE"])
@permission_classes((IsAuthenticated,))
def edelKategori(request, pk):
    data = request.data
    master = MasterKategori.objects.get(pk=pk)

    if request.method == "PUT":
        master.nama = data["nama"]
        master.save()
        return Response({"status": 200, "messages": "Data Berhasil Diubah!"})
    elif request.method == "DELETE":
        master.delete()
        return Response({"status": 200, "messages": "Data Berhasil Dihapus!"})
    
# Artikel
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getArtikel(request):
    judul = request.GET.get("judul")
    serializer = ArtikelSerializer(many=True)

    return Response(serializer.data)

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def createArtikel(request):
    data = request.data

    create = Artikel.objects.create(
        judul = data["judul"], 
        deskripsi=data["deskripsi"],
        detail=data["detail"]
    ) 
    create.save()

    return Response({"status":200, "messages" :  "Data Berhasil Ditambah!"})

@api_view(["PUT", "DELETE"])
@permission_classes((IsAuthenticated,))
def edelArtikel(request):
    data = request.data
    master = Artikel.objects.get()

    if request.method == "PUT":
        master.judul = data["judul"]
        master.deskripsi = data["deskripsi"]
        master.detail = data["detail"]

        master.save()
        return Response({"status": 200, "messages": "Data Berhasil Diubah!"})
    elif request.method == "DELETE":
        master.delete()
        return Response({"status": 200, "messages": "Data Berhasil Dihapus!"})

