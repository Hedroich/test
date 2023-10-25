from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        "message1" : "Заголовок первого уровня",
        "message2" : "Параграф с некоторым текстом"
    }
    return render(request, 'index.html', context)