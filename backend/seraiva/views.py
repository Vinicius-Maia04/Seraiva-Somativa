from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

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

class BookAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowingAPIView(ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
