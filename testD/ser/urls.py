from django.urls import path, include
from .routers import router
from .views import get_category, UserGenericAPIView, NewsGenericApiView

urlpatterns = [
    path("", include(router.urls)),
    path("cat/", get_category),
    path('users/<int:pk>', UserGenericAPIView.as_view(), name="users-list-get-update-delete"),
    path('news/<str:lan>', NewsGenericApiView.as_view(), name="news"),
    path('news/', NewsGenericApiView.as_view(), name="news"),
]
