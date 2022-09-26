from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    context = {}
    return render(request, 'library/index.html', context)


def media(request):
    context = {}
    return render(request, 'library/media-grid-view.html', context)


def blog(request):
    context = {}
    return render(request, 'library/blog.html', context)
