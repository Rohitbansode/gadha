from django.urls import path
from  . import views
from .views import data_view


urlpatterns = [
     path('', views.home ),
     path('data/',data_view, name='data'),

     path('add/', views.add_title, name='add_title'),
     path('era/', views.userapi),
]
