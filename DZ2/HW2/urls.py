"""
URL configuration for HW2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from HW2 import views
from django.urls import path

app_name = 'HW2'

urlpatterns = [
     # Путь для создания клиента
    path('create-client/', views.create_client_view, name='create_client'),
    # Путь для создания товара
    path('create-product/', views.create_product_view, name='create_product'),
    # Путь для создания заказа
    path('create-order/', views.create_order_view, name='create_order'),
]
