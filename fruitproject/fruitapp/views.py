from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Fruits


# Create your views here.
def home(request):
    return render(request,'home.html')

def product(request):
    product = Fruits.objects.all()
    context = {
        'product_list': product
    }
    return render(request, 'product.html', context)


def productdetail(request,product_id):
    product=Fruits.objects.get(id=product_id)
    return render(request,'detail.html',{'product':product})
def order(request):

    return render(request,'order.html')
def orderplaced(request):
    return render(request,'oderplaced.html')

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        auth.login(request,user)
        if user is not None:
            auth.login(request,user)
            return redirect('fruitapp:order')
        else:
            messages.info(request,'invalid')
            return  redirect('fruitapp:login')
    return render(request,'login.html')


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('fruitapp:register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request,'register success')
        else:
            messages.info(request, 'password not matched')
            return redirect('fruitapp:register')
        return redirect('fruitapp:login')
    return render(request,'register.html')


def logoutapp(request):
    print('logout')
    auth.logout(request)
    return redirect('/')