from django.urls import path
from . import views
from .views import BookDetailView ,AuthorDetailView, CategoryDetailView


app_name = "books"

urlpatterns = [
    path('books/', views.BooksView.as_view(), name ="books"),
    path('', views.Home.as_view(), name="home"),
    path('authors/', views.AuthorsView.as_view(), name ="authors"),
    path('categories/', views.CategoriesView.as_view(), name="categories"),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/detail/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('categories/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
