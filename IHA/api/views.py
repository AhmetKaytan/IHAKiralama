from django.shortcuts import render
from django.urls import reverse_lazy

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from IHA.models import IHA,Musteri,Kiralama
from IHA.api.serializers import IHASerializer, MusteriSerializer, KiralamaSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from ..forms import IHAForm,MusteriForm,KiralamaForm

class LoginView(APIView):
    template_name='../templates/registration/login.html'
    success_url=reverse_lazy('main')

class MainView(APIView):
    template_name ='../templates/main.html'

    def get (self,request,*args,**kwargs):
        return render(request,self.template_name)
    


##### Müşteri için Class based views#####
class MusteriListCreateApiView(APIView):
    #Listeleme işlemi
    def get(self, request):
        Musteriler = Musteri.objects.filter() #Burada nesnelerden oluşan bir quary set döner
        serializer = MusteriSerializer(Musteriler, many=True , context={'request': request})
        # return Response(serializer.data)
        context={'Musteriler':serializer.data}
        return render(request,'Musteriindex.html',context)
    
    #Create işlemi
    def post(self, request):
        serializer = MusteriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class MusteriDetailAPIView(APIView):
    def get_object(self, pk):
        Musteri_instance=get_object_or_404(Musteri, pk=pk)
        return Musteri_instance

    #Müşteri görüntüleme
    def get(self,request, pk):
        Musteri_instance=self.get_object(pk=pk)
        serializer = MusteriSerializer(Musteri_instance)
        context={'Musteri': Musteri_instance}
        return render(request, 'Musteridetail.html', context)
    
    #Update işlemi
    def put(self, request, pk):
        Musteri_instance=self.get_object(pk=pk)
        serializer = MusteriSerializer(Musteri_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #Silme işlemi
    def delete(self, request, pk):
        Musteri_instance=self.get_object(pk=pk)
        Musteri_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
##### IHA için Class based views ######
class IHAListCreateApiView(APIView):
    #Listeleme işlemi
    def get(self, request):
        IHAlar = IHA.objects.filter() 
        serializer = IHASerializer(IHAlar, many=True)
        context={'IHAlar':serializer.data}
        return render(request, 'IHAindex.html', context)
    #Create işlemi
    def post(self, request):
        serializer = IHASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class IHADetailAPIView(APIView):
    def get_object(self, pk):
        IHA_instance=get_object_or_404(IHA, pk=pk)
        return IHA_instance

    #IHA görüntüleme
    def get(self,request, pk):
        IHA_instance=self.get_object(pk=pk)
        serializer = IHASerializer(IHA_instance)
        context={'IHA':IHA_instance}
        return render(request, 'IHAdetail.html', context)
    
    #Update işlemi
    def put(self, request, pk):
        IHA_instance=self.get_object(pk=pk)
        serializer = IHASerializer(IHA_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #Silme işlemi
    def delete(self, request, pk):
        IHA_instance=self.get_object(pk=pk)
        IHA_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##### Kiralama işlemi için class based views#####
class KiralamaListCreateApiView(APIView):
    #Listeleme işlemi
    def get(self, request):
        Kiralamalar = Kiralama.objects.filter() 
        serializer = KiralamaSerializer(Kiralamalar, many=True , context={'request': request})
        context={'Kiralamalar':serializer.data}
        return render(request,'Kiralamaindex.html',context)
    
    #Create işlemi
    def post(self, request):
        serializer = KiralamaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class KiralamaDetailAPIView(APIView):
    def get_object(self, pk):
        Kiralama_instance=get_object_or_404(Kiralama, pk=pk)
        return Kiralama_instance
        
    #Kiralama görüntüleme
    def get(self,request, pk):
        Kiralama_instance=self.get_object(pk=pk)
        serializer = KiralamaSerializer(Kiralama_instance)
        context={'Kiralama':Kiralama_instance}
        return render(request, 'Kiralamadetail.html', context)    

    #Kiralama update
    def put(self, request, pk):
        Kiralama_instance=self.get_object(pk=pk)
        serializer = KiralamaSerializer(Kiralama_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #Kiralama silme
    def delete(self, request, pk):
        Kiralama_instance=self.get_object(pk=pk)
        Kiralama_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
