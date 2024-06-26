from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = CustomUser
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    categoryFK = CategorySerializer(read_only=True)
    class Meta:
        many = True
        model = Book
        fields = '__all__'

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Borrowing
        fields = '__all__'
