from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer
from rest_framework.permissions import IsAuthenticated


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateBook(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = [IsAuthenticated]

class RetrieveBook(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateBook(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteBook(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
