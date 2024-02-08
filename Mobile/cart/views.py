from django.shortcuts import render,redirect
from TodoApp.models import Product
from.models import Cart
from  django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    print(product)
    try:
        cart=Cart.objects.get(product=product)
        if cart.quantity<cart.product.stock:
            cart.quantity+=1
            cart.save()
            
        
        
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,product=product,quantity=1)
    return redirect('cart:displaycart')


def displaycart(req):
    user=req.session['user']
    cart=Cart.objects.all().filter(user=user)
    cart_items_count=Cart.objects.filter(user=req.user).count()

    return render(req,'cart.html',{'cart_items_count':cart_items_count,'cart':cart})



def cancelcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    if cart.quantity>1:
        cart.quantity-=1
        cart.save()
    return redirect('cart:displaycart')


def fullremove(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    cart.delete()
    return redirect('cart:displaycart')


def placeorder(req):
    user=req.session['user']
    cart=Cart.objects.filter(user=user)
    if product.product.stock -= product.product.quantity:
        product.save()
    for carts in cart:
        carts.delete()

    return redirect('cart:displaycart')