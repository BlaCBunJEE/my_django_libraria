from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import LibraryUser, Category, Author, BooksMedia
from django.views.generic import DetailView, ListView
from stocks import Books
import random


# Create your views here.
def signin(request):
    context = {}
    return render(request, 'library/signin.html', context)


def home(request):
    context = {}
    return render(request, 'library/index.html', context)


def media(request):
    all_books = BooksMedia.objects.all()[0:16]
    context = {'books': all_books}
    return render(request, 'library/media-grid-view.html', context)


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


class MediaDetail(DetailView):
    model = BooksMedia
    template_name = 'library/media-detail.html'
