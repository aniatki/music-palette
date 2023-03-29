from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from .models import Artwork, Creator
from django.contrib import messages

# Create your views here.


def products_view(request):
    """
    Rendering all products
    """
    artworks = Artwork.objects.all()
    creators = Creator.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No criteria entered to search')
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            artworks = artworks.filter(queries)

    context = {
        'artworks': artworks,
        'creators': creators,
        'search_query': query
    }
    return render(request, 'products.html', context)


def product_view(request, artwork_id):
    """
    Rendering a single product
    """
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    context = {'artwork': artwork}
    return render(request, 'product.html', context)
