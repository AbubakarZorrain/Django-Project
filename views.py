from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

def index(request):
    products = Product.objects.all().order_by('-id')[:9]
    outdoor_product = Product.objects.all().filter(category='Outdoor').order_by('-id')[:3]
    context={'products':products, 'outdoor_product':outdoor_product}
    return render(request,'e_comm_app/index.html', context)

def main(request):
    context={}
    return render(request,'e_comm_app/main.html', context)

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password Is Invalid.')
    context = {}
    return render(request, 'e_comm_app/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def shop(request):
    context={}
    return render(request,'e_comm_app/shop.html', context)

def about(request):
    context={}
    return render(request,'e_comm_app/about.html', context)

def blog(request):
    context={}
    return render(request,'e_comm_app/blog.html', context)

def blog_detail(request):
    context={}
    return render(request,'e_comm_app/blog-details.html', context)
@login_required(login_url='login')
def cart(request):
    context={}
    return render(request,'e_comm_app/cart.html', context)

def checkout(request):
    context={}
    return render(request,'e_comm_app/checkout.html', context)

def confirmation(request):
    context={}
    return render(request,'e_comm_app/confirmation.html', context)

def contact(request):
    context={}
    return render(request,'e_comm_app/contact.html', context)

def element(request):
    context={}
    return render(request,'e_comm_app/elements.html', context)

def product_details(request, slug):
   product= Product.objects.get(slug=slug)
   context={'product':product}
   return render(request,'e_comm_app/product_details.html', context)

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(request, 'e_comm_app/signup.html')
    else:
        form = UserCreationForm()
        context={form: 'form'}
    return render(request, 'e_comm_app/login.html', context)
@login_required(login_url='login')
def dashboard(request,):

    return render(request, 'e_comm_app/dashboard.html')



def register(request):
    if request.method == 'POST':
        form = RegCustomer(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/index',{'form': form})
    else:
        form = RegCustomer()
    return render(request, 'e_comm_app/signup.html', {'form': form})

def customers(request):
   customers= Customer.objects.all()
   products = Product.objects.all().filter(category='Outdoor').order_by('-id')[:3]
   context = {'products':products, 'cus':customers}
   return render(request,'e_comm_app/customer.html',context)




def upload_file(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'e_comm_app/contact.html',{'form': form})
    else:
        form = HotelForm()
    return render(request, 'e_comm_app/dashboard.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

#def upload_data(request, pk):
 #   order = ModelName.objects.get(id=pk)
  #  form= FormName(instance=order)
   # request.method == 'POST':
    #form = FormName(request.POST, instance=order)
    #if form.is_valid():
     #   form.save()
      #  return redirect('url/')
   # return render(request, ' url/', {'form':form})


def mainb(request):
    context={}
    return render(request,'e_comm_app/mainb.html', context)