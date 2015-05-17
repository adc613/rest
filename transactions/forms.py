from django import forms

from .models import Reservation, Order, OrderItem

class CreateReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['time','restuarant']

class CreateOrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['orderer','waiter']
    
    def clean_resturant(self):
        if restuarant.is_resturanat:
            raiseforms.ValidationError('Resturant is not a resturant')

class OrderItemCreationForm(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        fields = ['extras']
