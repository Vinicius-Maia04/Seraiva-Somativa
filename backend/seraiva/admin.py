from django.contrib import admin
from .models import *

# Register your models here.

class detAuthor(admin.ModelAdmin):
    list_display: ('id', 'email')
    list_display_links: ('id', 'email',)
    search_fields: ('email',)
    list_per_page = 10

admin.site.register(Author, detAuthor)

class detCategory(admin.ModelAdmin):
    list_display: ('id', 'name')
    list_display_links: ('id', 'name',)
    search_fields: ('name',)
    list_per_page = 10

admin.site.register(Category, detCategory)

class detBook(admin.ModelAdmin):
    list_display: ('id', 'name', 'price', 'edition')
    list_display_links: ('id', 'name',)
    search_fields: ('name',)
    list_per_page = 10

admin.site.register(Book, detBook)

class detBorrowing(admin.ModelAdmin):
    list_display: ('id', 'name', 'borrowingDate')
    list_display_links: ('id', 'name', 'borrowingDate',)
    search_fields: ('name',)
    list_per_page = 10

admin.site.register(Borrowing, detBorrowing)

class detCustomUser(admin.ModelAdmin):
    list_display: ('id', 'email', 'phoneNumber')
    list_display_links: ('id', 'email', 'phoneNumber',)
    search_fields: ('email',)
    list_per_page = 10

admin.site.register(CustomUser, detCustomUser)
