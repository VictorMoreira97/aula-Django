from blog import views
from django.urls import path

from . import views

urlpatterns = [
    path(', views.blog', name='blog'),
    path('exemplo1/', views.exemplo, names='exemplo'),
]