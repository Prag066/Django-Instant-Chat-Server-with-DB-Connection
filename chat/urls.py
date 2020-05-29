from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.logged_in,name='logged_in'),
    path('',views.index,name='index'),
    path('<str:user_name>/',views.room,name='room'),
]