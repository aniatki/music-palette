from django.shortcuts import render, get_object_or_404
from .models import Artwork, Creator

# Create your views here.


def artworks_view(request):
    """
    Rendering all products
    """
    artworks = Artwork.objects.all()
    creators = Creator.objects.all()
    return render(request, 'products.html', {
        'artworks': artworks,
        'creators': creators
        })


def artwork_view(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    return render(request, 'artwork.html', {'artwork': artwork})
