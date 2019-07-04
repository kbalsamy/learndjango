from django.urls import path
from .views import product_List, product_detail

app_name = 'shop'


urlpatterns = [path('', product_List, name='product_list'),
               path('<slug:catagory_slug>/', product_List, name='product_list_by_catagory'),
               path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
               ]
