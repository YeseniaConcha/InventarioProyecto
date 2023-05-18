from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from moduloApp.models import *


class TipoProductoForm(forms.Form):
    tipoProducto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcionTipoProducto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProductoForm(forms.Form):
    nombreProducto = forms.CharField(label="Nombre del producto",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(label="Cantidad de producto",
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    descripcionProducto = forms.CharField(label="Descripción del producto",
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    nombreProducto = forms.CharField(label="Nombre del producto",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(label="Cantidad de producto",
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    descripcionProducto = forms.CharField(label="Descripción del producto",
        widget=forms.TextInput(attrs={'class': 'form-control'}))





class BodegaForm(forms.Form):
    nombreBodega = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccionBodega = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

    nombreBodega = forms.CharField(label="Nombre de bodega",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccionBodega = forms.CharField(label="Dirección de bodega",
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProductoBodegaForm(forms.Form):
    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
