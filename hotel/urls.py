from django.urls import path

from . import views

urlpatterns = [  
    # homepage and links

    path('home/',views.home, name = 'home'),
    path('home/about/',views.about, name = 'about'),
    path('home/accomodation/',views.accomodation, name = 'accomodation'),
    path('home/contact/',views.contact, name = 'contact'),
    path('home/login/',views.login, name = 'login'),
    path('home/register/',views.register, name = 'register'),

    # routing

    path('/',views.homepage, name = 'homepage'),
    path('/rooms',views.room_lists, name = 'home'),
    path('/rooms/<uuid:room_id>',views.single_room, name = 'single_room'),
    path('/rooms/rooms/<uuid:room_id>/booking',views.room_booking, name = 'booking'),
    path('/rooms/<uuid:room_id>/booking/payment',views.payment, name = 'payment'),
    path('/rooms/<uuid:room_id>/checkin',views.room_checkin, name = 'room_checkin'),
    path('/rooms/<uuid:room_id>/checkout',views.room_checkout, name = 'room_checkout'),

    path('/login',views.admin_login, name = 'admin_login'),
    path('/login',views.dashboard, name = 'dashboard'),

    path('/admin',views.admin_list, name = 'admin_list'),
    path('/admin/create',views.admin_login, name = 'admin_create'),
    path('//admin/<uuid:staff_id>',views.show_admin, name = 'show_admin'),
    path('/admin/<uuid:staff_id>/edit',views.edit_admin, name = 'edit_admin'),
    path('/admin/<uuid:staff_id>/delete',views.delete_admin, name = 'delete_admin'),
    path('/admin/logs',views.logs, name = 'homepage'),

    





]


