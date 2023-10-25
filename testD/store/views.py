from django.shortcuts import render

from ser.serializers import CategorySerializer
from .models import Product
from .forms import ProductForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer


class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

def all_products(request):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'index_store.html', context)


def add(request):
    context = {
        "form": ProductForm,
    }
    if request.method == "POST":
        Product.objects.create(name=request.POST.get("name"), price=request.POST.get("price"))

    return render(request, 'add_product.html', context)


def base(request):
    return render(request, "base/base.html")


def child(request):
    return render(request, "base/child.html")


def main(request):
    return render(request, "main/main.html")


def task1(request):
    return render(request, "main/page1.html")


def task2(request):
    return render(request, "main/page2.html")