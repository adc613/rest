from django.db import models

# Create your models here.
class OrderItem(models.Model):
    menu_item = models.ForeignKey('menus.MenuItem')
    order = models.ForeignKey('transactions.Order', 
            related_name='items')
    extras = models.TextField()
   
class Order(models.Model):
    orderer = models.ForeignKey('accounts.User')
    waiter = models.ForeignKey('accounts.User', related_name='waiter')
    restuarant = models.ForeignKey('accounts.User',
            related_name='orders', null=True)
    tip = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    cost_of_food = models.DecimalField(max_digits=6, decimal_places=2,
            null=True)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, 
            null=True)

class Reservation(models.Model):
    time = models.DateTimeField()
    restuarant = models.ForeignKey('accounts.User')
    creator = models.ForeignKey('accounts.User', related_name='reservators')
