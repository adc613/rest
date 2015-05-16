from django.conf.urls import url

import views

urlpatterns = [
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^createuser/$', views.UserCreateView.as_view(), name='create_user'),
    url(r'^resturants/$', views.RestuarantListView.as_view(), name='restuarant_list'),
]
