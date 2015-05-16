from django.db import models

# Create your models here.
class OrderItem(models.Model):
    menu_item = models.ForeignKey('menus.MenuItem')
    order = models.ForeignKey('transactions.Order', 
            related_name='ordered_item')
    extras = models.TextField()
   
class Order(models.Model):
    orderer = models.ForeignKey('accounts.User')
    waiter = models.ForeignKey('accounts.User')
    restuarant = models.ForeignKey('account.User')
    tip = models.DecimalField(max_digits=6, decimal_places=2)
    cost_of_food = models.DecimalField(max_digits=6, decimal_places=2,
            blank=True)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, 
            blank=True)

class Reservation(models.Model):
    time = models.DateTimeField()
    restuarant = models.ForeignKey('accounts.User')
    reservee = models.ForeignKey('accounts.User', related_name='reservee')
