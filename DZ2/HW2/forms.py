from django import forms
from .models import Client, Product

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя клиента')
    email = forms.EmailField(label='Email клиента')
    phone_number = forms.CharField(max_length=15, label='Номер телефона клиента')
    address = forms.CharField(widget=forms.Textarea, label='Адрес клиента')

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название товара')
    description = forms.CharField(widget=forms.Textarea, label='Описание товара')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена товара')
    quantity = forms.IntegerField(label='Количество товара')

class OrderForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Выберите клиента')
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple, label='Выберите товары')
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Общая сумма заказа')
    order_date = forms.DateField(label='Дата оформления заказа')