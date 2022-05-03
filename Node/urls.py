from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_node),
    path('<str:name>', views.remove_node),
]