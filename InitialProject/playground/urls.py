from django.urls import path
from . import views

#URLConfiguration
urlpatterns = [
    path('open/', views.welcome)
]
