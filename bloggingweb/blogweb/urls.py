from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.print_hello, name='hello'),
    path('first_html/',views.first_html,name='firsthtml')
]