from django.db import models

# Create your models here.
class Order(models.Model):
    orderer = models.ForeignKey('accounts.models.User')
    restuarant = models.ForeignKey('accounts.models.User')
    menu_items = models.ManyToManyField('menu.models.menu_items')
    Menu = models.ForeignKey('menu.models.Menu')
    
class Reservations(models.Model):
    time = models.DateTimeField()
    restuarant = models.ForeignKey('accounts.models.User')
    user = models.ForeignKey('accounts.models.User')
