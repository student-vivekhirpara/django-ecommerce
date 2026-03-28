from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from project.models import *
from django.contrib import auth,messages
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from user.models import *
import os
# Create your views here.
def home(request):
    return render(request,'project/home.html',{})    

def dashboard(request):
    return render(request,'project/dashboard.html',{})

def header(request):
    return render(request,'project/header.html',{})    

def sidebar(request):
    return render(request,'project/sidebar.html',{})

def header(request):
    return render(request,'project/header.html',{}) 

# Category
def category(request):
    return render(request,'project/category.html',{})

def subcategory_edit(request,id):
    sub = Subcategory.objects.get(pk=id)
    cat = Category.objects.all()
    context = {'sub' : sub, 'cat': cat}
    return render(request, 'project/subcategory_edit.html',context)       

# Store
def category_store(request):
    name = request.POST['category_name'] 

    # SAVE TO Database

    Category.objects.create(name = name)
    return redirect('/project/category') 

# Read    
def category_table(request):
    cate = Category.objects.all()
    context = {'cate' : cate } 
    return render(request,'project/category_table.html',context)

# Delete
def delete(request,id):
    delit=Category.objects.get(pk=id)
    delit.delete()
    return redirect('/project/category_table')

# Upadate 
def category_update(request,id):
    name   = request.POST['category_name']

    data = {
        'name'    : name,
    }
        
    Category.objects.update_or_create(
        pk=id,defaults=data)
        
    return redirect('/project/category_table')   

# edit
def category_edite(request,id):
    cate = Category.objects.get(pk=id)    
    context = {'cate' : cate}
    return render(request, 'project/category_edite.html',context) 
             

# Subcategory
# ======================================================
def subcategory(request):
    cg = Category.objects.all()
    context = {'cg' : cg}
    return render(request,'project/subcategory.html',context)

# Store
def subcategory_store(request):
    subcategory = request.POST['subcategory_name']
    category_id = request.POST['name']

# SAVE TO Database
    Subcategory.objects.create( 
            subcategory = subcategory,
            name_id=category_id 
            )
    return redirect('/project/subcategory')    

# Read
def subcategory_table(request):
    sub = Subcategory.objects.all()
    context = {'sub' : sub}    
    return render(request,'project/subcategory_table.html',context) 

# Delete
def delete_sub(request,id):
    sub_dl=Subcategory.objects.get(pk=id)
    sub_dl.delete()
    return redirect('/project/subcategory_table')

# Edit
def subcategory_edit(request,id):
    sub = Subcategory.objects.get(pk=id)
    cat = Category.objects.all()
    context = {'sub' : sub, 'cat': cat}
    return render(request, 'project/subcategory_edit.html',context) 

# Update
def subcategory_update(request,id):
    subcategory  = request.POST['subcategory_name']
    name_id  = request.POST['name']

    sub_data = {
          'subcategory' : subcategory,
          'category_id' : name_id,  
    }
        
    Subcategory.objects.update_or_create(
        pk=id,defaults=sub_data)
        
    return redirect('/project/subcategory_table')


# Product
# =====================================
def product(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {'categories' : categories, 'subcategories' : subcategories}    
    return render(request,'project/product.html',context)

# Store
def product_store(request):
    category = request.POST['category_name']
    subcategory = request.POST['subcategory_name']
    product = request.POST['product_name']
    small_description = request.POST['small_description']
    large_description = request.POST['large_description']
    price = request.POST['price']
    image = request.FILES['product_img']
    status = request.POST['is_active']
    quantity = request.POST['quantity']

    Product.objects.create(
        category_id = category,
        subcategory_id = subcategory,
        product =product,
        small_des = small_description,
        large_des = large_description,
        price = price,
        image = image.name,
        status = status,
        quantity = quantity,
    )
                 
    mylocation = os.path.join(settings.MEDIA_ROOT,'images')
    obj = FileSystemStorage(location=mylocation)
    obj.save(image.name,image)

    return redirect('/project/product')

# Read
def product_table(request):
    read = Product.objects.all()
    context = {'read' : read}
    return render(request,'project/product_table.html',context)

# Details
def product_details(request,id):
    product = Product.objects.get(pk=id)
    context = {'product' :product }
    return render(request,'project/details.html',context)    

# Delete
def product_delete(request,id):
    Delete = Product.objects.get(pk=id)
    Delete.delete()
    return redirect('/project/product_table')      

# Edit & Update
def product_edit(request,id):
    edit = Product.objects.get(pk=id)
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {'edit' : edit, 'category' : category, 'subcategory' : subcategory}
    return render(request,'project/product_edit.html',context)  

# Update
def product_update(request,id):
    category = request.POST['category_name']
    subcategory = request.POST['subcategory_name']
    product = request.POST['product_name']
    small_des = request.POST['small_description']
    large_des = request.POST['large_description']
    price = request.POST['price']
    status = request.POST['is_active']
    quantity = request.POST['quantity']
    
    

    Updating_Data = {
        'category_id' : category,
        'subcategory_id' : subcategory,
        'product' : product,
        'small_des' : small_des,
        'large_des' : large_des,
        'price' : price,
        'status' : status,
        'quantity' : quantity,
    }


    if 'product_image' in request.FILES:
        image = request.FILES['product_image']
        mylocation = os.path.join(settings.MEDIA_ROOT,'images')
        obj = FileSystemStorage(location=mylocation)
        obj.save(image.name,image)
        Updating_Data['image'] = image
    
    Product.objects.update_or_create(
        pk=id, defaults= Updating_Data 
    ) 

    return redirect('/project/product_table')
# ==============================================================


# State
# ===========================
def state(request):
    return render(request,'project/state.html',{})

# Store
def state_store(request):
    state = request.POST['state_name']
    
    State.objects.create(
        state = state,
    )
    return redirect('/project/state')

# Read
def state_table(request):
    st = State.objects.all()
    context = {'st' : st }
    return render(request,'project/state_table.html',context)    

# Delete
def state_delete(request,id):
    Delete = State.objects.get(pk = id)
    Delete.delete()
    return redirect('/project/state_table')

# Edite
def state_edite(request,id):
    ed =  State.objects.get(pk = id)
    context = {'ed' : ed}
    return render(request, 'project/state_edite.html', context)

# Update
def state_update(request,id):
    state = request.POST['state_name']

    data = {
        'state' : state,
    }

    State.objects.update_or_create(
        pk = id,  defaults = data
    )
    return redirect('/project/state_table') 

    
# City
# ===========================================
def city(request):
    state=State.objects.all()
    context ={'state' : state}
    return render(request,'project/city.html',context)

# Store
def city_store(request):
    city = request.POST['city_name']
    state_id = request.POST['state']

# SAVE TO Database
    City.objects.create( 
            city = city,
            state_id=state_id 
            )
    return redirect('/project/city')

# Read
def city_table(request):
    ct = City.objects.all()
    context = {'ct' : ct}    
    return render(request,'project/city_table.html',context)

# Delete
def city_delete(request,id):
    ct_dl=City.objects.get(pk=id)
    ct_dl.delete()
    return redirect('/project/city_table')

def city_edite(request,id):
    city = City.objects.get(pk=id)
    sat  = State.objects.all()
    context = {'city' : city, 'sat': sat}
    return render(request, 'project/city_edite.html',context) 

# Update
def city_update(request,id):
    city  = request.POST['city_name']
    state_id  = request.POST['state']

    data = {
          'city' : city,
          'state_id' : state_id,  
    }
        
    City.objects.update_or_create(
        pk=id,defaults=data)
        
    return redirect('/project/city_table')                        

# Area
def area(request):
    state = State.objects.all()
    city = City.objects.all()
    context = {'state' : state, 'city' : city}
    return render(request,"project/area.html", context)

# Store
def area_store(request):
    state = request.POST['state']
    city = request.POST['city']
    area = request.POST['area_name']

    Area.objects.create(
        state_id = state,
        city_id = city,
        area = area
    )
    return redirect('/project/area')

# Read
def area_table(request):
    rd = Area.objects.all()
    context = {'rd' : rd}
    return render(request,'project/area_table.html',context)

# Delete
def area_delete(request,id):
    delete = Area.objects.get(pk = id )
    delete.delete()
    return redirect('/project/area_table')

# Edit
def area_edit(request,id):
    edit = Area.objects.get(pk= id)
    state = State.objects.all()
    city = City.objects.all()
    context = {'edit' : edit, 'state' : state, 'city' : city}
    return render(request, 'project/area_edit.html', context)

# Area
def area_update(request,id):
    state = request.POST['state']
    city = request.POST['city']
    area = request.POST['area_name']

    data = {
        'state_id' : state,
        'city_id' : city,
        'area' : area
    }
    Area.objects.update_or_create(
        pk = id,defaults = data
    )
    return redirect('/project/area_table')

def inquiry_list(request):
    inquiries = Inquiry.objects.all()
    context = {'inquiries': inquiries}
    return render(request, 'project/inquiry.html', context)

def register_table(request):
    show = Profile.objects.all()
    context = {'show': show}
    return render(request,'project/register_table.html',context)   

def feedback(request):
    show = Feedback.objects.all()
    context = {'show': show}
    return render(request,'project/feedback.html',context)    

def user(request):
    user = Profile.objects.all()
    return render(request,'project/user.html',{'user':user})   