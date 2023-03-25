from django.shortcuts import render
from .models import Artwork, Creator

# Create your views here.


def products(request):
    artworks = Artwork.objects.all()
    creators = Creator.objects.all()
    return render(request, 'products.html', {
        'artworks': artworks,
        'creators': creators
        })
