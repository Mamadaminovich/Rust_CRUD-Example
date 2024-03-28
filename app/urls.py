from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', home, name='home'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]