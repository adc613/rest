from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View

from .forms import CreateOrderForm, OrderItemCreationForm
from .models import Order

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
            form.save(commit=False)
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
        context = {}
        context['order'] = order
        context['form'] = self.form
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        item = OrderItemCreationForm(request.POST)
        if item.is_valid():
            rest = request.user
            order = Order.objects.get(pk='pk')
            item = item.save(commit=False)
            item.order = order
            item.save()

        return HttpResponseRedirect(reverse('transactions:add_item'))

