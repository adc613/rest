from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View


class CreateOrderView(View):
    template_name = 'transactions/create_oder.html'
    form = CreateOrderForm
    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, {'form':self.form})

    @method_decorator(login_required)
    def post(self, request):
        order = CreateOrderForm(request.POST)
        if order.is_valid() and request.user.is_restuarant:
            form.save(commit=False)
            order.restuarant = request.user
            form.save()
        return HttpResponseRedirect(reverse('home'))

class AddItemView(View):
   template_name = 'transactions/add_item.html'
   @method_decorator(login_required)
   def get(self, request, **kwargs):
       rest = request.user
       orders = rest.orders.all()
       return render(request, self.template_name, {'orders': orders})

    def post(self, request, **kwargs):

