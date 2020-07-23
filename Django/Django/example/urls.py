from django.urls import path

from . import views

urlpatterns = [
    path('checkbalance', views.checkbalance, name='checkbalance'),
    path('displaybalance', views.displaybalance, name='displaybalance'),
    path('withdrawal', views.withdrawal, name='withdrawal'),
    path('displaywithdrawal', views.displaywithdrawal, name='displaywithdrawal'),
    path('deposit', views.deposit, name='deposit'),
    path('displaydeposit', views.displaydeposit, name='displaydeposit'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('displaychangepassword', views.displaychangepassword, name='displaychangepassword')
]