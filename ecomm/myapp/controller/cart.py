from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from myapp.models import Cart, product


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = product.objects.get(id=prod_id)
            if (product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Product is already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    
                    if product_check.qty >= prod_qty :
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product is succefully added"})
                    else:
                        return JsonResponse({'status': "Only "+ str(product_check.qty)+ "quantity Available"})
                        
            else:
                return JsonResponse({'status': "No Such product found"})
        else:
            return JsonResponse({'status': "You need to login-_-"})
        
    return redirect('/')

def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request, "layout/cart.html", context)

def updatecar(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty =  int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Successfully"})
        else:
            return JsonResponse({'status': "No such product found"})
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "Delete from cart"})
    return redirect('/')

    

