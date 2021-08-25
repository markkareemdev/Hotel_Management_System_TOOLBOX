from django.urls import path

from . import views

urlpatterns = [  
    path('home/',views.home, name = 'home'),
    path('home/about/',views.about, name = 'about'),
    path('home/accomodation/',views.accomodation, name = 'accomodation'),
    path('home/contact/',views.contact, name = 'contact'),
    path('home/login/',views.login, name = 'login'),
    path('home/register/',views.register, name = 'register')
]


