from django.conf.urls import url

import views

urlpatterns = [
    url(r'^create/', views.CreateOrderView.as_view(), name='create_order'),
    url(r'^add/(?P<pk>\d+)', views.AddItemView.as_view(), name='add_item'),
    url(r'^list/', views.OrderListView.as_view(), name='order_list'),
    url(r'^complete/(?P<pk>\d+)', views.CompleteOrderView.as_view(), 
        name='complete'),
    url(r'^createreservation/(?P<pk>\d+)', views.CreateReservationView.as_view(),
        name='create_reservation'),
    url(r'^UpcominReservationsP/', views.ReservationListView.as_view(),
        name='reservation_list'),
]
