from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import views as users_views

urlpatterns = [  
    # routing: moshood part

    # path('/',views.homepage, name = 'homepage'),
    # path('/rooms',views.room_lists, name = 'home'),
    # path('/rooms/<uuid:room_id>',views.single_room, name = 'single_room'),
    # path('/rooms/rooms/<uuid:room_id>/booking',views.room_booking, name = 'booking'),
    # path('/rooms/<uuid:room_id>/booking/payment',views.payment, name = 'payment'),
    # path('/rooms/<uuid:room_id>/checkin',views.room_checkin, name = 'room_checkin'),
    # path('/rooms/<uuid:room_id>/checkout',views.room_checkout, name = 'room_checkout'),

   
    ##### sunday

    path('', views.homepage, name='hotel-home'),
    path('about/', views.about, name='hotel-about'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('admin', views.admin_list, name='admin-list'),

    path('admin/create', users_views.admin_create, name='register'),
    path('profile/', users_views.profile, name='profile'),

    path('/admin/create', views.admin_create, name='admin-create'),
    path('/admin/<uuid:staff_id>', views.show_admin, name= 'admin-staff'),
    path('/admin/<uuid:staff_id>/edit', views.edit_admin, name= 'admin-staff-edit'),
    path('/admin/<uuid:staff_id>/delete', views.delete_admin, name='admin-staff-delete'),

    path('login', auth_views.LoginView.as_view(template_name = 'hotel/login.html'), name= 'admin-login'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'hotel/logout.html'), name= 'admin-logout'),

    # addition
    path('/admin/logs',views.logs, name = 'logs')


]


