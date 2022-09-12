
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('db1', views.db1),
    path('db2', views.db2),
    path('db3', views.db3),
    path('db4', views.db4),
    path('about', views.about)
]