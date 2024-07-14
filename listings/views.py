from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm


def home(request):
    return render(request, 'index.html')

def cars(request):
    cars = Listing.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'listings.html', context)

def car(request, id):
    car = Listing.objects.get(id=id)
    context = {
        'car': car
    }
    return render(request, 'listing.html', context)

def create(request):
    form = ListingForm
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
        return redirect('/cars')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def update(request, id):
    car = Listing.objects.get(id=id)
    form = ListingForm(instance=car)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=car, files=request.FILES)
        if form.is_valid:
            form.save()
        return redirect('/cars')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

def delete(request, id):
    car = Listing.objects.get(id=id)
    car.delete()
    return redirect('/cars')