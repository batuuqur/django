from django.urls import path
from . import views

# http://127.0.0.1:8000 => index
# http://127.0.0.1:8000 => details
# http://127.0.0.1:8000 => list

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('<int:category_id>', views.getProductsByCategoryId),
    path('<str:category>', views.getProductsByCategory, name='products_by_category')
]