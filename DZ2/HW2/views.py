from django.shortcuts import render, redirect
from django.http import HttpResponse
from .crud import create_client, create_product, create_order
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm

# Пример представления для создания клиента
def create_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            registration_date = form.cleaned_data['registration_date']
            client = create_client(name, email, phone_number, address, registration_date)
            return HttpResponse(f'Client {client.name} created successfully!')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

# Пример представления для создания товара
def create_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            date_added = form.cleaned_data['date_added']
            product = create_product(name, description, price, quantity, date_added)
            return HttpResponse(f'Product {product.name} created successfully!')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

# Пример представления для создания заказа
def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            products = form.cleaned_data['products']
            total_amount = form.cleaned_data['total_amount']
            order_date = form.cleaned_data['order_date']
            order = create_order(client, products, total_amount, order_date)
            return HttpResponse(f'Order for {order.client.name} created successfully!')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})