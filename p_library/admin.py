from django.contrib import admin
from .models import Book, Author, Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass