from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView

from .forms import UserCreationForm
from .models import User

def logout_view(request):
    print 'start'
    logout(request)
    print 'done'
    return HttpResponseRedirect(reverse('home'))

class LoginView(View):
    template_name = 'accounts/login.html'
    def get(self,request):
        return render(request, self.template_name,{})

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request,user)

        return HttpResponseRedirect(reverse('home'))
        
class UserCreateView(View):
    template_name = 'accounts/create_user.html'
    form = UserCreationForm
    def get(self,request):
        context = {'form' : self.form }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You're now a user")

        messages.error(request, "didn't work bitch")
        return HttpResponseRedirect(reverse('home'))

class RestuarantListView(View):
    template_name = 'accounts/restuarant_list.html'
    def get(self, request):
        rests = User.objects.filter(is_restuarant=True)
        context = {'rests' : rests}
        return render(request, self.template_name, context)
