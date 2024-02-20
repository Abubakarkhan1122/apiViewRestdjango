from django.contrib import admin
from django.urls import path,include
from home import views
from .views import *
from rest_framework.views import APIView
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('student-list', views.student_list, name='student_list'),
    path('student-details/<int:id>', views.student_details, name='student_details'),
    path('book-list', views.book_list, name='book_list'),
    path('book-details/<int:id>', views.book_details, name='book_details'),
    path('food-list', views.food_list, name='food_list'),
    path('food-details/<int:id>', views.food_details, name='food_details'),

]