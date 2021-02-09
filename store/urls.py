from .views import index,signup
from django.urls import path

urlpatterns = [
    path('',index),
    path('signup',signup)
]   