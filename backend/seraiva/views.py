from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CustomUserAPIView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class AuthorAPIView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class BookAPIView(ModelViewSet):
    queryset = Book.objects.filter(stats=3)
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'categoryFK']

class BorrowingAPIView(ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
