from django.conf.urls import url

import views

urlpatterns = [
    url(r'^create/', views.CreateMenuView.as_view(), name='create_menu'),
    url(r'^createmenuitem/(?P<menu_pk>\d+)', views.CreateMenuItemView.as_view(),
        name='create_menu_item'),
    url(r'^itemlist/(?P<menu_pk>\d+)', views.MenuItemListView.as_view(), 
        name='menu_item_list'),
]
