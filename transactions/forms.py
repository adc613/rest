from django import forms

from .models import Reservation, Order

class ReservationCreationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['time','Restuarant','user']

    def clean_resturant(self):
        if restuarant.is_resturanat:
            raiseforms.ValidationError('Resturant is not a resturant')

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['orderer', 'restuarant', 'menu_items', 'menu']
    
    def clean_resturant(self):
        if restuarant.is_resturanat:
            raiseforms.ValidationError('Resturant is not a resturant')

    def save(self, commit=True):
        food_cost = 0
        order = super(OrderForm, self).save(commit=False)
        items = order.ordered_item.all()
        for item in items:
            food_cost += menu_item.price
        order.total_cost = food_cost + order.tip
       if commit:
           return order.save()
       return order

