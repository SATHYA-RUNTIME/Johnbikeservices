
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register',views.register),
    path('service',views.service),
    path('owner',views.owner),
    path('login',views.login,name="login"),
    path('status',views.status,name="status"),
    path('prebook',views.prebook),
    path('worker',views.worker),
    path('crud',views.crud,name="crud"),
    path('editbooking',views.editbooking),
    path('editdata/<id>',views.editdata),
    path('updatedetai/<id>',views.updatedetai),
    path('deletedata/<id>',views.deletedata),
    path('adminlog',views.adminlog),
    path('createservice',views.createservice),
    path('changeflag/<id>',views.changeflag),
    path('alluserservice/<id>',views.alluserservice),
    path('alldetail',views.alldetail),
    path('allservices',views.allservices),

]
