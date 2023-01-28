from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('search=<search_item>/', views.search),
    path('person/<pk>/', views.detail, name='detail'),
]