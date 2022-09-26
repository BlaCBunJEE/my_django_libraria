from django.shortcuts import render, redirect


# Create your views here.
def signin(request):
    context = {}
    return render(request, 'library/signin.html', context)


def home(request):
    context = {}
    return render(request, 'library/index.html', context)


def media(request):
    context = {}
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



