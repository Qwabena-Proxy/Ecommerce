from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from time import sleep
from .models import Machine

# Create your views here.
def indexPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = auth.authenticate(username= username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials..!')
            return redirect('/login')
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def logoutPage(request):
    print(f'{request.user} has logged out')
    auth.logout(request)
    return redirect('/')

def newProducts(request):
    if request.method == 'POST':
        new_product_name= request.POST['machineName']
        new_product_price= request.POST['machinePrice']
        new_product_description= request.POST['machineDescription']
        new_product_negotiatable= request.POST['machineNegotiatable']
        new_product_Image= request.FILES['machineImage']

        check= False
        if new_product_negotiatable != 'no':
            check= True

        new_product= Machine(machineName= new_product_name, machinePrice=new_product_price, machineDescription=new_product_description, machineNegotiatable=check, machineImage=new_product_Image)
        new_product.save()
        return redirect('/')
    else:
        return render(request, 'new_products_upload.html')