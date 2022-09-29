from django.shortcuts import render, redirect
from .models import LibraryUser, Category, Author, BooksMedia


# Create your views here.
def signin(request):
    context = {}
    return render(request, 'library/signin.html', context)


def home(request):
    context = {}
    return render(request, 'library/index.html', context)


def media(request):
    all_books = BooksMedia.objects.all()[0:12]
    category = Category.objects.all()
    context = {'books': all_books, 'categories': category}
    return render(request, 'library/media-grid-view.html', context)


def media_list(request):
    all_books = BooksMedia.objects.all()[0:12]
    category = Category.objects.all()
    context = {'books': all_books, 'categories': category}
    return render(request, 'library/media-list-view.html', context)


def mediadetail(request, pk):
    requested_book = BooksMedia.objects.get(id=pk)
    context = {'requested_book': requested_book}
    return render(request, 'library/media-detail.html', context)



def blog(request):
    context = {}
    return render(request, 'library/blog.html', context)


def services(request):
    context = {}
    return render(request, 'library/services.html', context)


def contact(request):
    context = {}
    return render(request, 'library/contact.html', context)


def cart(request):
    context = {}
    return render(request, 'library/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'library/checkout.html', context)
