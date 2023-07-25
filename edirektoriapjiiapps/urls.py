from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from edirektoriapjiiapps.api import views, masterdata

app_name = "authentication"
urlpatterns = [
    # ==== Authentication ====
    # path("signin/", users.signIn, name="signin"),

    # # ==== Users ====
    # path("getdataprofile/", views.MasterProfileView.as_view(), name="getdataprofile"),
    # path("createprofile/", users.createProfile, name="createprofile"),
    # path("edelprofile/<str:pk>", users.edelProfile, name="edelprofile"),
    # path("getprofile/", users.getProfile, name="getprofile"),

    # # <==== Master Satuan ====>
    # path('createsatuan/', masterdata.createSatuan, name='createsatuan'),
    # path('edelsatuan/<str:pk>', masterdata.edelSatuan, name='edelsatuan'),
    # path('getdatasatuan/', views.MasterSatuanView.as_view(), name='getdatasatuan'),
    # path("getsatuan/", masterdata.getSatuan, name="getSatuan"),

    # <==== Master Kategori ====>
    path('createkategori/', masterdata.createKategori, name='createkategori'),
    path('edelkategori/<str:pk>', masterdata.edelKategori, name='edelkategori'),
    path('getdatakategori/', views.MasterKategoriView.as_view(), name='getdatakategori'),
    path("getkategori/", masterdata.getKategori, name="getKategori"),

     # <==== Artikel ====>
    path('createArtikel/', masterdata.createArtikel, name='createArtikel'),
    path('edelArtikel/<str:pk>', masterdata.edelArtikel, name='edelArtikel'),
    path('getdataArtikel/', views.ArtikelView.as_view(), name='getdataArtikel'),
    path("getArtikel/", masterdata.getArtikel, name="getArtikel"),   

#    # <==== Master Cast ====>
#     path('createperusahaan/', masterdata.createPerusahaan, name='createperusahaan'),
#     path('edelperusahaan/<str:pk>', masterdata.edelPerusahaan, name='edelperusahaan'),
#     path('getdataperusahaan/', views.MasterPerusahaanView.as_view(), name='getdataperusahaan'),
#     path("getperusahaan/", masterdata.getPerusahaan, name="getPerusahaan"),
#     path("changeimageperusahaan/<str:pk>", masterdata.changeImagePerusahaan, name="changeimageperusahaan"),

#     # <==== Master Produk ====>
#     path('createproduk/', produk.getProduk, name='createproduk'),
#     path('edelproduk/<str:pk>', produk.edelProduk, name='edelproduk'),
#     path('getdataproduk/', views.ProdukKatalogView.as_view(), name='getdataproduk'),
#     path("getproduk/", produk.getProduk, name="getProduk"),

#     # <==== Master Wilayah ====>
#     path('getprovinsi/', masterdata.getProvinsi, name='getprovinsi'),
#     path('getkotakab/', masterdata.getKotakab, name='getkotakab'),
#     path('getkecamatan/', masterdata.getKecamatan, name='getkecamatan'),
#     path('getkelurahan/', masterdata.getKelurahan, name='getkelurahan'),
#     path('getkodepost/', masterdata.getKodepost, name='getkodepost'),

] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)