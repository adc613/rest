from django.contrib import admin

from .models import Reservation, Order

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Order)
