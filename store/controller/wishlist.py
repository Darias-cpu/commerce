from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Product, Cart, Wishlist
from django.contrib.auth.decorators import login_required
from store.models import Wishlist
@login_required(login_url='/login')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {"wishlist": wishlist}
    return render(request,'store/wishlist.html', context)
def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if Wishlist.objects.filter(user=request.user, product_id=prod_id):
                    return JsonResponse({'status': "Product already exists"})

                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added successfully"})
            else:
                return JsonResponse({'status': 'Product does not exists'})



        else:
            return JsonResponse({'status':"You are not logged in!"})

    return redirect('/')
def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if Wishlist.objects.filter(user=request.user, product_id=prod_id):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status': "Product removed from wishlist"})
            else:
                Wishlist.objects.create(user=request.user, product_id=prod_id)
                return JsonResponse({'status': "Product not found in wishlist"})

        else:
            return JsonResponse({'status':"You are not logged in!"})
    return redirect('/')

