from django.contrib import admin
from .models import Author, BooksMedia, LibraryUser, Category, Cart, CartItem
# Register your models here.

admin.site.register(LibraryUser)
admin.site.register(BooksMedia)
admin.site.register(Author)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(CartItem)

