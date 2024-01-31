from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views={}
    views['about_me'] = aboutme.objects.all()
    views['services'] = service.objects.all()
    views['feedback'] = feedback.objects.all()
    views['package'] = ourpackage.objects.all()
    return render(request,'index.html',views)


def about(request):
    views={}
    views['feedback'] = feedback.objects.all()
    return render(request,'about.html',views)

def services(request):
    views = {}
    views['feedback'] = feedback.objects.all()
    return render(request,'services.html',views)

def portfolio(request):
    return render(request,'portfolio.html')


def pricing(request):
    return render(request,'price.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    views={}
    views['contactdetails']=contactus.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email= request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contactform.objects.create(
        name = name,
        email = email,
        subject = subject,
        message = message
        ).save()

    return render(request,'contact.html',views)