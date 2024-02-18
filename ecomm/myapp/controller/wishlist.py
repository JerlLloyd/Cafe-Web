from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from myapp.models import Wishlist, product

def wish_list(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'layout/wishlist.html', context)

def addtowish(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':"Product is already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product is added to wishlist"})
            else:
                return JsonResponse({'status': "No such product found"})
            
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')

def deleteitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id, user=request.user)
                
                wishlistitem.delete()
                return JsonResponse({'status':"Product removed from wishlist"})
            else:
                return JsonResponse({'status': "Product not found in wishlist"})
        else:
             return JsonResponse({'status':"Login to continue"})
            
    return redirect('/')