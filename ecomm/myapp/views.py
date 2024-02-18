from django.contrib import messages
from django.shortcuts import redirect, render

from .models import *


def home(request):
    return render(request, "app/index.html")

def collections(request):
    category = Category.objects.filter(status=0)
    context={'category': category}
    return render(request, "layout/collection.html", context)

def collectionsview(request, sid):
    if (Category.objects.filter(sid=sid, status=0)):
        products = product.objects.filter(category__sid=sid)
        category_n = Category.objects.filter(sid=sid).first()
        context = {"products": products, 'category_n':category_n}
        return render(request, "product/index.html", context)
    else:
        messages.warning(request, "no category found")
        return redirect('collections')

def productview(request, fat_sid, prod_sid):
    if(Category.objects.filter(sid=fat_sid, status=0)):
        if(product.objects.filter(sid=prod_sid, status=0)):
            products = product.objects.filter(sid=prod_sid, status=0).first()
            context = {'products': products }
        else:
            messages.error(request, "no such product exist")
            return redirect('collections')
    else:
        messages.error(request, "no such category exist")
        return redirect('collections')
    return render(request, "product/views.html", context)