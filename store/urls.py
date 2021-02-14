from .views import index,signup
from django.urls import path

urlpatterns = [
    path('',index,name='homepage'),
    path('signup',signup)
]   