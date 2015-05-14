from django.conf.urls import url

import views

urlpatterns = [
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^createuser/$', views.UserCreateView.as_view(), name='create_user'),
]
