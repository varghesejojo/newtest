from django.urls import path
from . import views
app_name='fruitapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.product,name='product'),
    path('order',views.order,name='order'),
    path('orderplaced',views.orderplaced,name='orderplaced'),
    path('productdetail/<int:product_id>/',views.productdetail,name='productdetail'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logoutapp',views.logoutapp,name='logoutapp'),


]
