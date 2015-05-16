from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View

from .forms import MenuCreationForm, MenuItemCreationForm
from .models import Menu, MenuItem

class CreateMenuView(View):
    template_name='menus/create_menu.html'
    form = MenuCreationForm

    def get(self,request):
        return render(request, self.template_name, {'form':self.form})
    
    @method_decorator(login_required)
    def post(self, request):
        form = MenuCreationForm(request.POST)
        user = request.user
        print 'start'
        if form.is_valid() and user.is_restuarant:
            print 'step'
            menu = form.save(commit=False)
            menu.restuarant = user
            menu.save()
            print "success"
        else:
            print "error"

        
        return HttpResponseRedirect(reverse('home'))

class CreateMenuItemView(View):
    template_name = 'menus/create_menu_item.html'
    form = MenuItemCreationForm

    def get(self,request, **kwargs):
        menu = Menu.objects.get(pk = kwargs['menu_pk'])
        context = {}
        context['menu'] = menu
        context['form'] = self.form
        if request.user == menu.restuarant:
            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect(reverse('home'))

    def post(self,request, **kwargs):
        menu = Menu.objects.get(pk = kwargs['menu_pk'])
        form = MenuItemCreationForm(request.POST)
        print 'step'
        if form.is_valid() and request.user == menu.restuarant:
            print 'step2'
            menu_item = form.save(commit=False)
            menu_item.menu = menu
            menu_item.save()
            print 'success'

        return HttpResponseRedirect(reverse('home'))
        
class MenuItemListView(View):
    template_name = 'menus/menu_item_list.html'
    def get(self, request, **kwargs):
        menu_pk = kwargs['menu_pk']
        print 'life'
        print menu_pk
        items = MenuItem.objects.filter(menu__pk = menu_pk)
        return render(request, self.template_name, {'items':items})
