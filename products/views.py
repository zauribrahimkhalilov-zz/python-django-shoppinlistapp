from django.shortcuts import render

# Create your views here.
from products.models import Products


def index(request):
    products = Products.objects.all()[:10]
    context = {'title': 'ShoppingList App', 'products':products }
    return render(request, 'products/product.html', context)

def product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        product = Products(name=name)
        product.save()
        products = Products.objects.all()[:10]
        context = {'title': 'ShoppingList App', 'products':products}
        return render(request, 'products/product.html', context)