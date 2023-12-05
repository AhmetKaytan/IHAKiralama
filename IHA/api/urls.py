from django.urls import path
from IHA import views
from IHA.api import views as api_views

urlpatterns = [
    path('main/',api_views.MainView.as_view(), name='Anasayfa'),
    path('IHAlar/',api_views.IHAListCreateApiView.as_view(), name='IHA_listesi'),
    path('IHAlar/<int:pk>',api_views.IHADetailAPIView.as_view(), name='IHA_detay'),
    path('Musteriler/',api_views.MusteriListCreateApiView.as_view(), name='Musteri_listesi'),
    path('Musteriler/<int:pk>',api_views.MusteriDetailAPIView.as_view(), name='Musteri_detay'),
    path('Kiralamalar/',api_views.KiralamaListCreateApiView.as_view(), name='Kiralama_listesi'),
    path('Kiralamalar/<int:pk>',api_views.KiralamaDetailAPIView.as_view(), name='Kiralama_detay'),
]

#####Function based views url#####
# urlpatterns = [
#     path('IHAlar/',api_views.IHA_list_create_api_view, name='IHA_listesi'),
#     path('IHAlar/<int:pk>',api_views.IHA_detail_api_view, name='IHA_detay'),
# ]