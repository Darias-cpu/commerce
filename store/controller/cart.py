
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Product, Cart
from django.contrib.auth.decorators import login_required

def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            # Safely retrieve product ID and quantity
            prod_id = int(request.POST.get('product_id'))
            # Check if the product exists
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                # Check if the product is already in the cart
                if Cart.objects.filter(user=request.user.id, product_id=prod_id):
                    return JsonResponse({'status': "Product Already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                # Check if the requested quantity is available
                if product_check.quantity >= prod_qty :
                    # Create a new cart item
                    Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                    return JsonResponse({'status': "Product added successfully"})
                else:
                    # Not enough quantity available
                    return JsonResponse({'status': "Only"+ str(product_check.quantity) + "quantity available"})
            else:
                # Product doesn't exist
                return JsonResponse({'status': "No such product found"})
        else:
            # User is not authenticated
            return JsonResponse({"status": "Please log in to continue"})

    # If the request is not POST, redirect to home page
    return redirect('/')
@login_required(login_url='/login')
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart': cart}
    return render(request, "store/cart.html",context)
def updatecart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('prod_qty', 1))
            cart = Cart.objects.get(user=request.user, product_id=prod_id)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Product updated successfully"})
    return redirect('/')
def deletecartitem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(user=request.user, product_id=prod_id)
            cartitem.delete()
            return JsonResponse({'status': "Product deleted successfully"})
        return redirect('/')

