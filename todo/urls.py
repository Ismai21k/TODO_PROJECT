from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('del/<str:item_id>/', views.remove, name ='del'),
    
]