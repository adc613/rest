from django.contrib import admin

from .models import Reservation, Order, OrderItem

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(OrderItem)
