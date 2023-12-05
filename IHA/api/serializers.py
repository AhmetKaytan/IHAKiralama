from rest_framework import serializers
from IHA.models import IHA, Musteri, Kiralama

######IHA modeli için Model Serializer######
class IHASerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = '__all__'

         
###### Müşteri için Model Serializer######
class MusteriSerializer(serializers.ModelSerializer):
    IHAlar =serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='IHA_detay'
    )
    class Meta:
        model = Musteri
        fields = '__all__'

##### Kiralama işlemleri için Model Serializer######
class KiralamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kiralama
        fields = '__all__'


