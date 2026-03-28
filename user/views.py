from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.core.mail import send_mail
from django.db import transaction
from django.conf import settings
from project.models import *
from user.models import *
import os
import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'user/home.html')

def base(request):
    return render(request,'user/base.html',{})   

def header(request):
    return render(request,'user/header.html',{})

def footer(request):
    return render(request,'user/footer.html',{}) 

# /*----------------------------------------*/
# /* Change Password
# /*----------------------------------------*/
def change_password(request):
    return render(request,'user/change_password.html',{})      

def change_password_check(request):
        username    = request.user.username
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = auth.authenticate(
            username = username,
            password = old_password
        )
        if user is None:

            return redirect('/user/change_password')
        
        else:

            user.set_password(new_password)
            user.save() 
            return redirect('/user/login') 

# /*----------------------------------------*/
# /* Forgate Password
# /*----------------------------------------*/            

def forgate_password(request):
    return render(request,'user/forgate_password.html',{}) 

def forgate_password_check(request):
    email = request.POST['email']

    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        profile = Profile.objects.get(user_id=user.id)
        password = profile.password

        mysubject = "Password Reset Request"
        mymessage = "Your Password is :"+password
        myfrom  = 'vivekhirpara43@gmail.com'
        myto    = ['email'] 

        send_mail(mysubject,mymessage,myfrom,myto)
        messages.info(request,"Your Password is sent to your email id")
        return redirect('/user/login')

    else:
        messages.error(request,"Email Not Found in our Records")
        return redirect('/user/forgate_password')     


# # /*----------------------------------------*/
# # /* Inquiry Form
# # /*----------------------------------------*/

def inquiry(request):
    return render(request,'user/inquiry.html',{})
    
def inquiry_store(request):
    name    = request.POST['name']
    email   = request.POST['email']
    contact = request.POST['contact']
    message = request.POST['message']

    Inquiry.objects.create(
        name    = name,
        email   = email,
        contact = contact,
        message = message
    )

    return redirect('/user/inquiry')

# # /*----------------------------------------*/
# # /*  Registration Form 
# # /*----------------------------------------*/ 

def register(request):
    return render(request,'user/register.html',{})

# Register Store

def register_store(request):
    # Auth User Fields 
    first_name = request.POST['f_name']
    last_name = request.POST['l_name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
      # Profile Fields
    contact = request.POST['contact']


    if password == confirm_password:
        user =  User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = password
        )
        
        Profile.objects.create(
            contact = contact,
            password = password,
            user_id = user.id
        )
        return redirect('/user/login')
    
    else:
        return redirect('/user/register')


# # /*----------------------------------------*/
# # /*  Login  Form 
# # /*----------------------------------------*/ 

def login(request):
    return render(request,'user/login.html',{})

def login_verify(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = auth.authenticate(
            username = username, 
            password = password
            )

        if user is not None:
            # User exists → login and redirect to home
            auth.login(request, user)
            return redirect('/user/home')
        else:
            # User invalid → show error and redirect back to login
            messages.error(request, "Username or password is incorrect!")
            return redirect('/user/login')
    else:
        return redirect('/user/login')
    
# # /*----------------------------------------*/
# # /*  Log Out 
# # /*----------------------------------------*/ 

def logout(request):
    auth.logout(request)
    return redirect('/user/login')

# # /*----------------------------------------*/
# # /*  Profile 
# # /*----------------------------------------*/        

def profile(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    context = {'profiles':profiles}
    return render(request,"user/Profile.html", context )

# /*----------------------------------------*/
# /*  Feedback 
# /*----------------------------------------*/ 

def feedback(request):
    return render(request, 'user/feedback.html') 

def feedback_store(request):
    rating = request.POST['rating']
    message = request.POST['message'] 
    user = request.user.id

    Feedback.objects.create(
        rating = rating,
        message = message,
        user_id = user
    )
    messages.success(request, "Thank you for your feedback!")    
    return redirect('/user/feedback')

# /*----------------------------------------*/
# /*  User Profile 
# /*----------------------------------------*/ 
def user_profile(request):
    profile = Profile.objects.get(user_id = request.user.id)
    context = {'profile':profile}
    return render(request,"user/user.html", context ) 

def edit_profile(request):
    profile = Profile.objects.get(user_id =request.user.id)
    context = {'profile':profile}
    return render(request,'user/edit_profile.html',context)       

def update_profile(request):
    id = request.user.id
    profile = Profile.objects.get(user_id=id).id
    first_name = request.POST['f_name'] 
    last_name  = request.POST['l_name']
    email      = request.POST['email']
    username   = request.POST['username']
    contact    = request.POST['contact']
    
    update_data = {
        'first_name':first_name,
        'last_name' : last_name,
        'email' : email,
        'username': username,
    }
    data = {
        'contact' : contact,
    }
    User.objects.update_or_create(
         pk = request.user.id, defaults = update_data
        )
    Profile.objects.update_or_create(pk=profile,defaults=data)
    return redirect('/user/user_profile')

# /*----------------------------------------*/
# /* Shop wala Page
# /*----------------------------------------*/     

def product(request):
    show = Product.objects.all()
    context = {'show' : show}
    return render(request,'user/product.html',context)

def shop_detail(request,id):
    show = Product.objects.get(pk=id)
    context = {'show' : show}
    return render(request,'user/shop_detail.html',context) 

# /*----------------------------------------*/
# /* Cart Page
# /*----------------------------------------*/             

def add_cart(request,id):
    product = Product.objects.get(pk=id)
    quantity = request.POST.get('qty',1)
    
    Cart.objects.create(
        product=product,
        user_id=request.user.id,
        quantity=quantity,
        price=product.price 
        )
    return redirect('/user/cart')

def cart(request):
    cart = Cart.objects.filter(user_id=request.user.id)

    item_total=0
    for i in cart:
        i.item_total = i.quantity * i.price

    total_amount = 0 
    for i in cart:
        total_amount += i.quantity * i.price

    return render(request,"user/cart.html",{'cart':cart, 'total_amount':total_amount})        

def update_cart(request,id):
    cart = Cart.objects.get(pk=id)

    if request.method == "POST":
        action = request.POST.get('action')

        if action == 'plus':
            cart.quantity +=1
        elif action == 'minus' and cart.quantity>1:
            cart.quantity -=1

        cart.save()

    return redirect('/user/cart')
     
# Remove button
def cart_delete(request,id):
    cart = Cart.objects.get(pk=id)     
    cart.delete()
    return redirect('/user/cart')
    
# /*----------------------------------------*/
# /* Checkout Page
# /*----------------------------------------*/   

def product_checkout(request):
    cart = Cart.objects.filter(user_id = request.user.id)
    item_total = 0 

    for i in cart:
        i.item_total = i.quantity * i.price

    total_amount = sum(i.quantity * i.product.price for i in cart)
    request.session['total_amount'] = float(total_amount)
    context = {'cart' : cart,'total_amount':total_amount }

    return render(request,'user/checkout.html',context)  
                         

# /*----------------------------------------*/
# /* Place Page
# /*----------------------------------------*/     
def place_order(request):
    cart = Cart.objects.filter(user_id=request.user.id)

    if request.method == "POST":
        total_amount = sum(item.price for item in cart)

        order = Order.objects.create(
            amount=total_amount,
            customer_id=request.user.id,
            status='pending'
            )

        for item in cart:
            Order_details.objects.create(
                order_id=order.id,
                product_id=item.product.id,
                price=item.price,
                quantity=item.quantity
            )   
        
        Billing_detail.objects.create(
            customer_id=request.user.id,
            order_id=order.id,
            first_name=request.POST['billing_first_name'],
            last_name=request.POST['billing_last_name'],
            contact=request.POST['billing_contact'],
            email=request.POST['billing_email'],
            address1=request.POST['billing_address'],
            city=request.POST['billing_city'],
            state=request.POST['billing_state'],
            pincode=request.POST['billing_pincode'],
        )

        Shipping_details.objects.create(
            first_name=request.POST['shipping_first_name'],
            user_id=request.user.id,
            order_id=order.id,
            last_name=request.POST['shipping_last_name'],
            contact=request.POST['shipping_contact'],
            email=request.POST['shipping_email'],
            address=request.POST['shipping_address'],
            city=request.POST['shipping_city'],
            state=request.POST['shipping_state'],
            pincode=request.POST['shipping_pincode'],
        )

        payment_method = request.POST.get('payment_method')
        if payment_method == "cod":
            order.status = "confirmed"
            order.save()
        elif payment_method == "online":
            order.status = "confirmed"
            order.save()
            cart.delete()
            return redirect('/user/payment_process')

        cart.delete()

        return redirect('/user/home')
    return redirect('/user/product_checkout')

def payment_process(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    amount = int(request.session['total_amount'])*100

    client = razorpay.Client(auth=(key_id, key_secret))

    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"OIBP",
        "notes":{
            'name' : 'AK',
            'payment_for':'OIBP Test'
        }
    }
    id = request.user.id
    result = User.objects.get(pk=id)
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result}
    return render(request, 'user/payment_process.html',context)

@csrf_exempt
def success(request):
    context = {}
    return render(request,'user/success.html',context) 

def order(request):
    order = Order.objects.filter(customer_id=request.user.id)
    order_details = Order_details.objects.filter(order_id__in=order)
    context = {'order':order,'order_details':order_details}
    return render(request,'user/order.html',context)      