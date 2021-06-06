from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.views import loginView
from accounts.forms import UserProfileForm, SignUpForm

def homeView(request):
    context = {}
    return render(request, 'ecomm/index.html', context)

def productView(request, id):
    prod = Product.objects.get(id = id)
    context = {
        'prod': prod,
    }

    return render(request, 'ecomm/product.html', context)


@login_required 
def profileView(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    context = {
        "form" : form
    }
    return render(request,"ecomm/profile.html",context)

