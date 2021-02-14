from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer



# Create your views here.
def index(request):
    products = None
    categories =Category.get_all_categories()
    categoryID= request.GET.get('category')    
    if categoryID:
        products=Product.get_all_products_by_categoryid(categoryID)
    else:
        products=Product.get_all_products()
    data= {}
    data['products']= products
    data['categories']= categories
    return render(request,'index.html',data)

def validateCustomer(customer):
    error_message=None;

    if(not customer.first_name):
        error_message="First Name Required"
    elif len(customer.first_name)<4 :
        error_message= "First name should be minimum 4 character "
    elif  not customer.last_name:
        error_message="Lastname Required!!"
    elif len(customer.last_name)<4:
        error_message="Last name should be minimum 4 character "
    elif not customer.phone:
        error_message='Phone Number Required!!'
    elif len(customer.phone)<10:
        error_message="Phone number must be minimum 10 digit"
    elif len(customer.password)<8:
        error_message="password must be minimum 8 character"
    elif len(customer.email)<6:
        error_message="email must be minimum 6 character"
    elif customer.isExists():
        error_message='Email Address Already Registered'
    return error_message

def registerUser(request):
      
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')

        # validation
        value={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'phone':phone
        }

        error_message=None

        customer= Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message=validateCustomer(customer)
        # saving
        if not error_message:
            print(first_name,last_name,phone,email,password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data)



def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        return registerUser(request)