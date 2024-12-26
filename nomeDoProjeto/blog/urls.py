from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<id>', views.blog, name='post'),
    path('exemplo1/', views.exemplo, names='exemplo'),
]