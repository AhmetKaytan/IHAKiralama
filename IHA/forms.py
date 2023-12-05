from django import forms
from .models import IHA,Musteri,Kiralama

class IHAForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = '__all__'


class MusteriForm(forms.ModelForm):
    class Meta:
        model = Musteri
        fields = '__all__'


class KiralamaForm():
    class Meta:
        model = Kiralama
        fields = '__all__'