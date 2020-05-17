from django.shortcuts import render
from django.views.generic.base import  View
from django.views.generic.detail import DetailView

from .models import Book, Author, Category

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books_list.html", {"books_list": books})


class Home(View):
    def get(self, request):
        return render(request, "books/home.html")


class AuthorsView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, "books/authors_list.html", {"authors_list": authors})


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "books/categories_list.html", {"categories_list": categories})

class BookDetailView(DetailView):
    queryset = Book.objects.all()
    context_object_name = 'book'
    slug_field = 'pk'
    template_name = 'books/books_detail.html'


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    context_object_name = 'author'
    slug_field = 'pk'
    template_name = 'books/authors_detail.html'

class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    context_object_name = 'category'
    slug_field = 'pk'
    template_name = 'books/categories_detail.html'