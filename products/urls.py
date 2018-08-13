from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]
