from django.contrib import admin
from .models import Booking, Payment, PaymentType, Receptionist, Room, RoomStatus, RoomType, User

admin.site.register(User)
admin.site.register(Receptionist)
admin.site.register(RoomType)
admin.site.register(RoomStatus)
admin.site.register(Room)
admin.site.register(PaymentType)
admin.site.register(Payment)
admin.site.register(Booking)
