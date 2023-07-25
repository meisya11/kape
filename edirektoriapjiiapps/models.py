from django.db import models

# Create your models here.

class MasterKategori(models.Model):
    nama = models.CharField(max_length = 100)

    def __str__(self):
        return self.nama

class Artikel(models.Model):
    judul = models.CharField(max_length = 250)
    kategori = models.ForeignKey(MasterKategori, on_delete=models.SET_NULL,null=True)
    tanggal = models.DateField()
    gambar = models.CharField(max_length = 250)
    deskripsi = models.CharField(max_length=500)
    detail = models.CharField(max_length = 250)

    def __str__(self):
        return self.judul

