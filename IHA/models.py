from django.db import models
from time import time


class IHA(models.Model):
    marka = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    agirlik = models.IntegerField()
    kategori = models.CharField(max_length=150)

    def __str__(self):
        return self.model

class Musteri(models.Model):
    sirket_ismi = models.CharField(max_length=150)
    ulke = models.CharField(max_length=150)
    telefon_no = models.CharField(unique=True,max_length=13)
    adres = models.TextField(max_length=250)
    kayit_tarihi = models.DateField(auto_now=True)
    kiralanmis_IHAlar = models.ManyToManyField('IHA', through='Kiralama')

    def __str__(self):
        return self.sirket_ismi
    
class Kiralama(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    IHA = models.ForeignKey(IHA, on_delete=models.CASCADE)
    kiralama_tarihi = models.DateField()
    kiralama_saati = models.TimeField(default="00:00:00")
    kiralama_suresi = models.IntegerField()  #Gün cinsinden
    kiralama_ucreti = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"{self.musteri} - {self.IHA} - {self.kiralama_tarihi}"