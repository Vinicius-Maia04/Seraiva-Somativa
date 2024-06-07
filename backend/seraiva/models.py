from .manager import * 
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.

JOB = {
    ('0','user'),
    ('1','librarian'),
    ('2','author'),
    ('3','admin')
}

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    phoneNumber = models.CharField(max_length=15)
    job= models.CharField(max_length=30, choices=JOB)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = "email" #substituir o login username por e-mail
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.email    

class Author(models.Model):
    customUserFK = models.ForeignKey(CustomUser, related_name='customUserAuthorFK',on_delete=models.CASCADE)
    picture = models.CharField(max_length=500)
    biography= models.TextField()

    def __str__(self):
        return self.customUserFK.email



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
BOOK_FORMAT = {
    ('1','Fisico'),
    ('2','E-Book')
}

STATUS = {
    ('1','Pendente'),
    ('2','Cancelado'),
    ('3','Aprovado')
}

STARS = {
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
}

class Book(models.Model):
    # userFK
    categoryFK = models.ForeignKey(Category, related_name="BookCategoryFK", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField()
    format = models.TextField(max_length=30, choices=BOOK_FORMAT)
    edition = models.IntegerField()
    releaseDate = models.DateField()
    stats = models.CharField(max_length=30,choices=STATUS)
    stars = models.CharField(max_length=30,choices=STARS)

    def __str__(self):
        return self.name
    
class Borrowing(models.Model):
    bookFK = models.ForeignKey(Book,related_name="bookFKBorrowing",on_delete=models.CASCADE)
    # userFK
    borrowingDate = models.DateField(auto_now=True)
    devolutionDate = models.DateField()
    returnedDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.bookFK.name


    
    
    
    
    


