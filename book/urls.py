from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.BookList.as_view()),
    path('createbook', views.CreateBook.as_view()),
    path('rbook/<int:pk>', views.RetrieveBook.as_view()),
    path('updatebook/<int:pk>', views.UpdateBook.as_view()),
    path('deletebook/<int:pk>', views.DeleteBook.as_view()),
]