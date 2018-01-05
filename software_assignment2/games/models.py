# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    genre_type = models.CharField(max_length=100)
    bool_genre= models.BooleanField()

    def __str__(self):
        return str(self.id_genre) + "-" + self.genre_type



class Game(models.Model):
    id_game = models.AutoField(primary_key=True)
    game_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=50)
    game_year = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    bool_game = models.BooleanField()

    def __str__(self):
        return str(self.id_game) + "-" + self.game_name




class Developer(models.Model):
    id_developer = models.AutoField(primary_key=True)
    developer_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    developer_name = models.CharField(max_length=40)
    bool_developer = models.BooleanField()

    def __str__(self):
        return str(self.id_developer) + "-" + self.developer_name

