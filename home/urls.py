from .views import *
from django.urls import path, include

urlpatterns = [
    path('',home,name='home'),
    path('about',about,name='about'),
    path('services', services, name='services'),
    path('portfolio', portfolio, name='portfolio'),
    path('pricing', pricing,name='pricing'),
    path('blog', blog,name='blog'),
    path('contact',contact, name='contact')

]