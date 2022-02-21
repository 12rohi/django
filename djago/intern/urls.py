from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    #for registration
    path("Register/", views.register, name="Register"),

    #for customers
    path('customers/',views.customers, name="customers"),

    #for history
    path('history/',views.history, name="history"),

    #for details
    path('details/',views.details, name="details")

]