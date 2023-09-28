from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone
# from phones.import_phones import Phones
from django.template.defaultfilters import slugify


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('price').reverse()
    else:
        phone_objects = Phone.objects.all()
    context = {'phones':phone_objects}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'  
    phone_objects = Phone.objects.filter(slug=slug)
    context = {'phones': phone_objects}
    return render(request, template, context)
