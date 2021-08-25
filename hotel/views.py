from django.http import HttpResponse
from django.shortcuts  import render


def home(request):
    return render(request,'hotel/index.html')
def about(request):
    return render(request,'hotel/about.html')
def accomodation(request):
    return render(request,'hotel/accomodation.html') 
def contact(request):
    return render(request,'hotel/contact.html')
def login(request):
    return render(request,'hotel/login.html')
def register(request):
    return render(request,'hotel/register.html')
 
