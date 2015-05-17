from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    menu = models.ForeignKey('menus.Menu', related_name='items')

class Menu(models.Model):
    restuarant = models.ForeignKey('accounts.User', related_name='menu')
    title = models.CharField(default="menu", max_length=255)

    def get_absolute_url(self):
        return reverse('menus:menu_item_list', kwargs= {'menu_pk':self.pk})
