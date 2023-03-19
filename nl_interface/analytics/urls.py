from django.urls import path
from . import views


from django.http import HttpResponse


urlpatterns = [
    path('', views.index, name='index'),
    path('create_matter/', views.create_matter, name='create_matter'),
    path('matter_detail/<int:matter_id>/', views.matter_detail, name='matter_detail'),
    path('matters/', views.matters, name='matters'),
]