from django.urls import path
from . import views

urlpatterns = [
    path('open/', views.welcome),
    path('version/', views.check_version),
    path('getname/', views.send_name_object)   
]
