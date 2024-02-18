from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from myapp.models import Cart, Order, OrderItem, product
from myapp.views import productview
import random


def checks(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.qty :
            Cart.objects.delete(id=item.id)
            
            
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.s_price * item.product_qty
        
    context = {'cartitems':cartitems, 'total_price':total_price}
    return render(request, "layout/checkout.html", context)

def placeorder(request):
    if request.method == 'POST':
        neworder = Order()
        neworder.user =  request.user
        neworder.Fname = request.POST.get('Fname')
        neworder.Lname = request.POST.get('Lname')
        neworder.Email = request.POST.get('Email')
        neworder.Contact = request.POST.get('Contact')
        neworder.Address = request.POST.get('Address')
        neworder.Baranggay = request.POST.get('Baranggay')
        neworder.City = request.POST.get('City')
        neworder.Pincode = request.POST.get('Pincode')
        
        neworder.payment_mode = request.POST.get('payment_mode')
        
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.s_price * item.product_qty
        
        neworder.total_price = cart_total_price
        trackno = 'CATasthropic Cafe '+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = trackno = 'CATasthropic Cafe '+ str(random.randint(1111111,9999999))
            
        neworder.tracking_no = trackno
        neworder.save()
        
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
            order=neworder,
            product=item.product,
            price=item.product.s_price,
            quantity=item.product_qty,
        )

        orderproduct = product.objects.filter(id=item.product_id).first()
        orderproduct.qty = orderproduct.qty - item.product_qty
        orderproduct.save()
        
        Cart.objects.filter(user=request.user).delete()
        
        messages.success(request, "Your order  has been placed successfully")


    return redirect('/')
