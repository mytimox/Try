from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from .models import PIB
from .form import PIBForm
from products.models import Product, ProductImage


def landing(request):
    name = PIB.objects.get(id=1)
    return render(request, 'landing/landing.html', {'name1':name})


def form(request):
    if request.method == 'POST':
        form=PIBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lalka:landing'))
    else:
        form=PIBForm()
    return render (request,'landing/form.html', {'form':form})

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', {'products_images':products_images})