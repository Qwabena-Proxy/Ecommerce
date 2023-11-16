from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime, timedelta
from time import sleep
from .models import *
from pathlib import Path
import os

# Create your views here.
def indexPage(request):
    result= []
    machine = Machine.objects.all()
    category = MachineCategory.objects.all()
    brands = MachineBrand.objects.all()
    brandimages = BrandImages.objects.all()
    if request.method == 'POST':
        machines = Machine.objects.all()
        categorys = MachineCategory.objects.all()
        brands = MachineBrand.objects.all()

        category= request.POST['category']
        brand= request.POST['brand']
        price= request.POST['price']
        for machine in machines:
            if category == str(machine.machineCategory) or brand == str(machine.machineBrand) or price == str(machine.machinePrice):
                result.append(machine)
            else:
                pass
        context = {
        'machines': machines,
        'brands': brands,
        'categorys': categorys,
        'results': result,
        'images' : brandimages
    }
        return render(request, 'index.html', context= context)
    else:
        context = {
        'machines': machine,
        'brands': brands,
        'categorys': category,
        'images' : brandimages
    }
        return render(request, 'index.html', context= context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = auth.authenticate(username= username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials..!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logoutPage(request):
    print(f'{request.user} has logged out')
    auth.logout(request)
    return redirect('/')

def newProducts(request):
    if request.user.is_authenticated:
        machine = Machine.objects.all()
        category = MachineCategory.objects.all()
        brands = MachineBrand.objects.all()
        context = {
        'machines': machine,
        'brands': brands,
        'categorys': category,
    }
        if request.method == 'POST':
            new_product_name= request.POST['machineName']
            new_product_price= request.POST['machinePrice']
            new_product_description= request.POST['machineDescription']
            new_product_Image= request.FILES['machineImage']
            new_product_Brand= request.POST['machineBrand']
            new_product_Category= request.POST['machineCategory']
            try:
                new_product_negotiatable= request.POST['machineNegotiatable']
            except:
                new_product_negotiatable= 'uncompleted'
          
            check= False
            if new_product_negotiatable != 'uncompleted':
                check= True
            
            # Retrieve the MachineCategory instance based on the 
            for category in category:
                if new_product_Category == str(category):
                    new_product_Category = category
                else:
                    pass

            for brand in brands:
                if new_product_Brand == str(brand):
                    new_product_Brand = brand
                else:
                    pass
            # print(check)
            new_product= Machine(machineName= new_product_name, machinePrice=float(new_product_price), machineDescription=new_product_description, machineNegotiatable=check, machineImage=new_product_Image, machineBrand=new_product_Brand, machineCategory=new_product_Category, user= request.user)
            new_product.save()
            return redirect('/')
        else:
            return render(request, 'new_products_upload.html', context= context)
    else:
        return redirect('/')

def updateProduct(request, productid, productname):
    if request.method == 'POST':
        machine= Machine.objects.all()
        new_product_name= request.POST['machineName']
        new_product_price= request.POST['machinePrice']
        new_product_description= request.POST['machineDescription']
        new_product_Brand= request.POST['machineBrand']
        new_product_Category= request.POST['machineCategory']
        try:
            new_product_negotiatable= request.POST['machineNegotiatable']
        except:
            new_product_negotiatable= 'uncompleted'
        try:
            new_product_Image= request.FILES['machineImage']
        except:
            new_product_Image= ''
        
        check= False
        if new_product_negotiatable != 'uncompleted':
                check= True

        if new_product_Image == '':
            category = MachineCategory.objects.all()
            brands = MachineBrand.objects.all()
            # Retrieve the MachineCategory instance based on the 
            for category in category:
                if new_product_Category == str(category):
                    new_product_Categorys = category
                else:
                    pass

            for brand in brands:
                if new_product_Brand == str(brand):
                    new_product_Brands = brand
                else:
                    pass

            print(new_product_Brands, new_product_Categorys)
            product = get_object_or_404(Machine, id= productid)
            product.machineName= new_product_name
            product.machinePrice=float(new_product_price)
            product.machineDescription=new_product_description
            product.machineNegotiatable=check
            product.machineBrand=new_product_Brands
            product.machineCategory=new_product_Categorys
            product.user= str(request.user)
            product.save()

        else:
            old= machine.get(id= productid)
            oldimagepath= old.machineImage
            oldimagepath= f'{os.getcwd()}\media\{oldimagepath}'
            oldimagepath= os.path.normpath(oldimagepath)
            # print(oldimagepath)
            print('Removing old image')
            os.remove(path=f'{oldimagepath}')
            print('Completed')

            category = MachineCategory.objects.all()
            brands = MachineBrand.objects.all()
            # Retrieve the MachineCategory instance based on the 
            for category in category:
                if new_product_Category == str(category):
                    new_product_Categorys = category
                else:
                    pass

            for brand in brands:
                if new_product_Brand == str(brand):
                    new_product_Brands = brand
                else:
                    pass

            print(new_product_Brands, new_product_Categorys)
            product = get_object_or_404(Machine, id= productid)
            product.machineName= new_product_name
            product.machinePrice=float(new_product_price)
            product.machineImage= new_product_Image
            product.machineDescription=new_product_description
            product.machineNegotiatable=check
            product.machineBrand=new_product_Brands
            product.machineCategory=new_product_Categorys
            product.user= str(request.user)
            product.save()
            
        return redirect('index')
        
    else:
        category = MachineCategory.objects.all()
        brands = MachineBrand.objects.all()
        product_to_be_updated= Machine.objects.get(id= productid, machineName= productname)
        context= {
            'product': product_to_be_updated,
            'brands': brands,
            'categorys': category,
        }
        return render(request, 'update.html', context= context)

def deleteProduct(request, productid, productname):
    if request.method == 'POST':
        old= Machine.objects.get(id= productid)
        oldimagepath= old.machineImage
        oldimagepath= f'{os.getcwd()}\media\{oldimagepath}'
        oldimagepath= os.path.normpath(oldimagepath)
        data= Machine.objects.filter(id= productid).delete()
        print('Removing old image')
        os.remove(path=f'{oldimagepath}')
        print('Completed')
        print(data)
        return redirect('index')

    else:
        product= Machine.objects.get(id= productid, machineName= productname)
        context= {
            'product': product,
        }
        return render(request, 'delete.html', context= context)

def brandimageAdd(request):
    return render(request, 'brandimage.html')

def brandAdd(request):
    return render(request, 'brand.html')

def categoryAdd(request):
    return render(request, 'category.html')

def productDetails(request, productid, productname):
    product= Machine.objects.get(id= productid, machineName= productname)
    context= {
        'product': product,
    }
    return render(request, 'details.html', context= context)

def tails(request):
    machine= Machine.objects.all()
    context= {
        'machine': machine,
    }
    return render(request, 'tails.html', context=context)

def products(request):
    machine= Machine.objects.all()
    context= {
        'machine': machine,
    }
    return render(request, 'allproducts.html', context=context)