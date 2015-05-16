from django.db import models

# Create your models here.
class Order(models.Model):
    orderer = models.ForeignKey('accounts.models.User')
    menu_items = models.ManyToManyField('menu.models.menu_items')
    menu = models.ForeignKey('menu.models.Menu')
    tip = models.DecimalField(max_digits=6, decimal_places=2)
    
    
class Reservations(models.Model):
    time = models.DateTimeField()
    restuarant = models.ForeignKey('accounts.models.User')
    user = models.ForeignKey('accounts.models.User')
