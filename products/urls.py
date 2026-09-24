from django.urls import path

from . import views

app_name = 'products'

urlpatterns=[
    path('',views.home,name='home'),
    path('store/',views.store_page,name='store_page'),
    path('store/<slug:category_slug>/',views.store_page,name='product_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>',views.product_detail,name='product_detail_page'),
]