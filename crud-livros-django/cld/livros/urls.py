from django.urls import path

from .import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.livro_list, name='livro_list'),
]
