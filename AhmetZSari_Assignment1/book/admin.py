# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Book, Author
from django.contrib import admin

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
