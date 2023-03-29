from django.shortcuts import render
from products.models import Artwork, Creator

# Create your views here.

def index(request):
    artworks = Artwork.objects.all()
    context = {
        'artworks': artworks,
    }
    return render(request, 'home/index.html', context)