"""
Views module serving the index page
"""


from django.shortcuts import render
from products.models import Artwork, Creator

# Create your views here.


def index(request):
    """
    Serving the home view
    """
    artworks = Artwork.objects.all()
    creators = Creator.objects.all()
    return render(request, 'home/index.html', {
        'artworks': artworks,
        'creators': creators
        })
