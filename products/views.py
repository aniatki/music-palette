from django.shortcuts import render, get_object_or_404
from .models import Artwork, Creator

# Create your views here.


def products_view(request):
    """
    Rendering all products
    """
    artworks = Artwork.objects.all()
    creators = Creator.objects.all()
    context = {
        'artworks': artworks,
        'creators': creators
    }
    return render(request, 'products.html', context)


def product_view(request, artwork_id):
    """
    Rendering a single product
    """
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    context = {'artwork': artwork}
    return render(request, 'product.html', context)
