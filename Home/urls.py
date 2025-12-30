from django.contrib import admin
from django.urls import path
from Home import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='Home'),
    path("Authors", views.Authors, name='Authors'),
    path("About", views.About, name='About' ),
    path('categories/<str:key>', views.categories, name='categories'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:id>', views.dele, name='delete'),
    path('reco/<str:key>', views.reco, name='reco'),
]