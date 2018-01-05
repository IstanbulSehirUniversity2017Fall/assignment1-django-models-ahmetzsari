# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Genre, Game, Developer
from django.contrib import admin

# Register your models here.

admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Developer)
