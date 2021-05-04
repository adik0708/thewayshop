from django.urls import path
from .views import home, products, search, contact, category_detail, outfit_detail

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),
    path('category/<int:id>', category_detail, name='category_detail'),
    path('outfit/<int:id>', outfit_detail, name='outfit_detail')
]
