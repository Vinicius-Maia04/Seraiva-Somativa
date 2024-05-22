from rest_framework import serializers
from .models import *

class AuthorSerializer(Serializers.ModelSerializer):
    class Meta:
        many = True
        model = Author
        fields = '__all__'

class CategorySerializer(Serializers.ModelSerializer):
    class Meta:
        many = True
        model = Category
        fields = '__all__'

class BookSerializer(Serializers.ModelSerializer):
    class Meta:
        many = True
        model = Book
        fields = '__all__'

class BorrowingSerializer(Serializers.ModelSerializer):
    class Meta:
        many = True
        model = Borrowing
        fields = '__all__'

class CustomUserSerializer(Serializers.ModelSerializer):
    class Meta:
        many = True
        model = CustomUser
        fields = '__all__'