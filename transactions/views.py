from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.views.generic import View

import decimal

from .forms import CreateOrderForm, OrderItemCreationForm, CreateReservationForm
from .models import Order
from accounts.models import User
from menus.models import MenuItem

class CreateOrderView(View):
    template_name = 'transactions/create_order.html'
    form = CreateOrderForm
    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, {'form':self.form})

    @method_decorator(login_required)
    def post(self, request):
        form = CreateOrderForm(request.POST)
        if form.is_valid() and request.user.is_restuarant:
            form = form.save(commit=False)
            form.restuarant = request.user
            form.save()
        return HttpResponseRedirect(reverse('home'))

class AddItemView(View):
    template_name = 'transactions/add_item.html'
    form = OrderItemCreationForm
    @method_decorator(login_required)
    def get(self, request, **kwargs):
        order = Order.objects.get(pk=kwargs['pk'])
        items = order.items.all()
        menu = order.restuarant.menu.all()[0]
        menu_items = menu.items.all() 
        context = {}
        context['order'] = order
        context['items'] = items
        context['menu_items'] = menu_items
        context['form'] = self.form
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        item = OrderItemCreationForm(request.POST)
        if item.is_valid():
            rest = request.user
            order = Order.objects.get(pk=kwargs['pk'])
            item = item.save(commit=False)
            menu_item = MenuItem.objects.get(pk=request.POST['menu_item'])
            item.order = order
            item.menu_item = menu_item
            item.save()
            kwargs = {'pk': kwargs['pk']}

        return HttpResponseRedirect(reverse('transactions:add_item', 
            kwargs=kwargs))


class OrderListView(View):
    template_name = "transactions/order_list.html"
    def get(self, request):
        user = request.user
        if user.is_restuarant:
            orders = Order.objects.filter(restuarant__pk=user.pk)
            context = {'orders':orders}
            return render(request, self.template_name, context)
        else:
            order = Order.objects.filter(orderer__pk=user.pk)[0]
            return HttpResponseRedirect(reverse('transactions:complete',
                kwargs={'pk':order.pk}))

class CompleteOrderView(View):
    template_name = 'transactions/customer_complete.html'
    def get(self, request, **kwargs):
        context = {}
        order = Order.objects.get(pk=kwargs['pk'])
        items = order.items.all()
        context['items'] = items
        food_cost = decimal.Decimal(0)
        for item in items:
            food_cost = food_cost + item.menu_item.price
        context['food_cost'] = food_cost
        context['order'] = order
        return render(request, self.template_name,context)

    def post(self, request, **kwargs):
        order = Order.objects.get(pk=kwargs['pk'])
        if order.orderer == request.user:
            percent = decimal.Decimal(0.0)
            amount = decimal.Decimal(0.0)
            tip = decimal.Decimal(0.0)
            food_cost = decimal.Decimal(0)
            try:
               percent = request.POST['tip_percent']
            except MultiValueDictKeyError:
                pass
            try:
               amount = request.POST['tip_dollar']
            except MultiValueDictKeyError:
                pass
            items = order.items.all()
            for item in items:
                food_cost += item.menu_item.price
            if percent:
                tip = (food_cost * percent)
            elif amount:
                tip = amount
            else:
                tip = food_cost * decimal.Decimal(.20)
            total_cost = food_cost + tip
            order.cost_of_food = food_cost
            order.tip = tip
            order.total_cost = total_cost
            order.save()
            print 'success'
        
        return HttpResponseRedirect(reverse('home'))

class CreateReservationView(View):
    
    def post(self, request, **kwargs):
        reservation = CreateReservationForm(request.POST) 
        print 'start'
        if reservation.is_valid():
            user = request.user
            rest = User.objects.get(pk=kwargs['pk'])
            print kwargs['pk']
            print rest
            r = reservation.save(commit=False)
            r.creator = user
            r.restuarant = rest
            r.save()
            print 'success'

        return HttpResponseRedirect(reverse('home'))

class ReservationListView(View):
    template_name = 'transactions/reservation_list.html'
    def get(self, request):
        rest = request.user
        reservations = rest.reservations.all()
        context = {}
        context['reservations'] = reservations
        return render(request, self.template_name, context)
