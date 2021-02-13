from django.shortcuts import render
from django.http import HttpResponse
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

def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')

        # validation
        error_message=None

        if(not first_name):
            error_message="First Name Required"
        elif len(first_name)<4 :
            error_message= "First name should be minimum 4 character "
        elif  not last_name:
            error_message="Lastname Required!!"
        elif len(last_name)<4:
            error_message="Last name should be minimum 4 character "
        elif not phone:
            error_message='Phone Number Required!!'
        elif len(phone)<10:
            error_message="Phone number must be minimum 10 digit"
        elif len(password)<8:
            error_message="password must be minimum 8 character"
        elif len(email)<6:
            error_message="email must be minimum 6 character"

        # saving
        if not error_message:
            print(first_name,last_name,phone,email,password)
            customer= Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
            customer.register()
        else:
            return render(request,'signup.html',{'error':error_message})

