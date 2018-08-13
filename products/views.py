from django.shortcuts import render, get_object_or_404, redirect

from products.models import Products
from .forms import ProductForm
from django.views.generic import ListView, DetailView, View


class ProductListView(ListView):
    template_name = "products/product.html"
    queryset = Products.objects.all()

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        context = {'object_list': self.queryset, 'form': form}
        return render(request, self.template_name, context)


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Products, id=id_)


class ProductCreateView(View):
    template_name = "products/product.html"

    def get(self, request, *args, **kwargs):

        form = ProductForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
            queryset = Products.objects.all()
        context = {"form": form, 'object_list': queryset}

        return render(request, self.template_name, context)
