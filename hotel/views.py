from django.http import HttpResponse
from django.shortcuts  import render

# homepage and links handler

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
 
# routed urls handler

def homepage(request):
    pass
def room_lists(request):
    pass
def single_room(request):
    pass
def room_booking(request):
    pass
def payment(request):
    pass
def room_checkin(request):
    pass
def room_checkout(request):
    pass


def admin_login(request):
    pass
def dashboard(request):
    pass



def admin_list(request):
    pass
def admin_login(request):
    pass
def show_admin(request):
    pass
def edit_admin(request):
    pass
def delete_admin(request):
    pass
def logs(request):
    pass