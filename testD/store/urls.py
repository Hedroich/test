from django.urls import path
from .views import all_products
from .views import add, base, child, main, task1, task2, ProductApiView

urlpatterns = [
    path('', all_products),
    path('add/', add),
    path('base/', base),
    path('child/', child),
    path('main/', main),
    path('task1/', task1),
    path('task2/', task2),
    path("all/", ProductApiView.as_view(), name="product-list")
]
