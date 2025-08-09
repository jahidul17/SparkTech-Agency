from django.contrib import admin
from .models import Author, Book,Categories

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Categories)