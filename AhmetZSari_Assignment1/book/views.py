# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    all_books = Book.objects.all()
    html = ''
    for book in all_books:
        url = '/book/' + str(book.id) + '/'
        html += '<a href= "' + url +'">' + book.book_name + '</a> <br>'
    return HttpResponse(html)

def detail(request, book_id):
    return HttpResponse("<h2>Details for album id: " + str(book_id) + "</h2>")