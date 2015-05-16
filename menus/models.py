from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    menu = models.ForeignKey('menus.Menu')

class Menu(models.Model):
    restuarant = models.ForeignKey('accounts.User')
    title = models.CharField(default="menu", max_length=255)
