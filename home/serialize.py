from rest_framework import serializers
from .models import Student,Book,Food
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','age','father_name', 'description']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'title']


class FoodSerializer(serializers.ModelSerializer):
 class Meta:
     model = Food
     fields = ['id', 'name',  'taste']


