from django.shortcuts import render,redirect
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Useradd,Contact
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Product

def home(request):
    return render(request, 'bookpage.html')
# Create your views here.
def feed_back(request):
    return render(request,'feed_back.html')
def login_view(request):
    return render(request,'login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")
    #     return redirect("home")
    # return render(request,"login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        c = User.objects.create_user(username = username, email = email, password = password)
        c.save()
        return redirect("login_user")
    return render(request,"register.html")
    

def logout_user(request):
    logout(request)
    return redirect("home")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        c = Contact(name = name, email = email, message = message)
        c.save()
        return redirect("home")
    return render(request,"contact.html")


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Product, Cart

# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('view_cart')

# @login_required
# def view_cart(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     return render(request, 'cart.html', {'cart_items': cart_items})

# @login_required
# def remove_from_cart(request, product_id):
#     cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)
#     cart_item.delete()
#     return redirect('view_cart')

@login_required
def sell_books(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        description = request.POST['description']
        image = request.POST['image']

        new_book = Product(title=title, author=author, price=price, description=description, image=image)
        new_book.save()
        return redirect('home')
    return render(request, "sell_books.html")



