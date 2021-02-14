from .views import index,signup,login
from django.urls import path

urlpatterns = [
    path('',index,name='homepage'),
    path('signup',signup),
    path('login',login)
]   