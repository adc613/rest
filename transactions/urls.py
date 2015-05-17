from django.conf.urls import url

import views

urlpatterns = [
    url(r'^create/', views.CreateOrderView.as_view(), name='create_order'),
    url(r'^add/(?P<pk>\d+)', views.AddItemView.as_view(), name='add_item'),
]
