
from django.urls import path
from . import views

urlpatterns = [
    path('model/', views.add_model,name='add_model'),
    path('form/', views.add_form,name='add_form'),
   
]

