from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
from .models import Student, Book, Food
from .serialize import StudentSerializer, BookSerializer, FoodSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
def home(request):
    return HttpResponse("hello")
#for model Students
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
     student_obj = Student.objects.all()
     serializer = StudentSerializer(student_obj, many=True)
     return Response({"students": serializer.data})
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"status": "success","message": "data Edited successfully"})

@api_view(['GET', 'POST' , 'PUT', 'DELETE'])
def student_details(request,id):
 try:
     student = Student.objects.get(id=id)
 except Student.DoesNotExist:
     return Response(status=status.HTTP_404_NOT_FOUND)
 if request.method == 'PUT':
     serializer = StudentSerializer(student , data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response({"status": "success","message": "Student edited successfully"})
 if request.method == 'DELETE':
  if student.delete():
   return Response({"status": "success","message": "Student deleted"})

#for model book
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        book_obj = Book.objects.all()
        serializer = BookSerializer(book_obj, many=True)
        return Response({"books": serializer.data})
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","message": "data edited successfully"})

@api_view(['DElETE', 'PUT'])
def book_details(request,id):
 try:
  book = Book.objects.get(id=id)
 except Book.DoesNotExist:
    return Response(status= status.HTTP_404_NOT_FOUND)
 if request.method == 'PUT':
     serializer = BookSerializer(book, data= request.data)
     if serializer.is_valid():
         serializer.save()
         return Response({"status": "success","message": "data edited successfully"})

 if request.method == 'DELETE':
   if book.delete():
    return Response({"status": "success","message": "data deleted successfully"})

#for model food

@api_view(['GET','POST'])
def food_list(request):
    if request.method == 'GET':
        food_obj = Food.objects.all()
        serializer = FoodSerializer(food_obj, many=True)
        return Response({"foods": serializer.data})
    if request.method == 'POST':
        serializer = FoodSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","message": "data send successfully"})

@api_view(['PUT', 'DELETE'])
def food_details(request,id):
    if request.method == 'PUT':
        food_obj = Food.objects.get(id=id)
        serializer = FoodSerializer(food_obj, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success","message": "data edited successfully"})
    if request.method =='DELETE':
        food_obj = Food.objects.get(id=id)
        food_obj.delete()
        return Response({"status": "success","message": "data deleted successfully"})
