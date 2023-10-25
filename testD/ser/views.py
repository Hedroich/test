from django.contrib.auth.models import User
from .serializers import UserSerializer, CategorySerializer, NewsSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import Category
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView
from .mixins import LanguageMixin
from .models import News


# class NewsGenericApiView(GenericAPIView):
class NewsGenericApiView(GenericAPIView, LanguageMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get(self, request):
        data = super().change_language(request)
        if not data:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(data, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # def get(self, request):
    #     news = News.objects.filter(lan=request.query_params['lan'])
    #     if not news:
    #         return Response(status.HTTP_404_NOT_FOUND)
    #     serializer = NewsSerializer(news, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)


class UserGenericAPIView(RetrieveUpdateDestroyAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def get_category(request):
    category = Category.objects.all()
    if not category:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
