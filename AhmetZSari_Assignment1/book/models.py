# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genre =  models.CharField(max_length=100)
    book_cover =  models.CharField(max_length=1000)

class Author(models.Model):
    author_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_age = models.CharField(max_length=10)