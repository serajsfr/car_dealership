from django.shortcuts import render
from .models import Listing
from .forms import ListingForm


def listings(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context)

def listing(request, id):
    listing = Listing.objects.get(id=id)
    context = {
        'listing': listing
    }
    return render(request, 'listing.html', context)

def create(request):
    form = ListingForm
    context = {
        'form': form
    }
    return render(request, 'create.html', context)
