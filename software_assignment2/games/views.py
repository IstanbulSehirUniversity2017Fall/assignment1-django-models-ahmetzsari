# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Genre, Game, Developer
from django.http import Http404
# Create your views here.


def index(request):
    all_games = Game.objects.all()
    template = loader.get_template('games/index.html')
    context = {
        'all_games' : all_games,
    }
    return HttpResponse(template.render(context, request))


def genres(request):
    all_genres = Genre.objects.all()
    template = loader.get_template('games/genres.html')
    context = {
        'all_genres': all_genres,
    }
    return HttpResponse(template.render(context, request))

def games(request):
    all_games = Game.objects.all()
    template = loader.get_template('games/games.html')
    context = {
        'all_games': all_games,
    }
    return HttpResponse(template.render(context, request))

def developers(request):
    all_developers = Developer.objects.all()
    template = loader.get_template('games/developer.html')
    context = {
        'all_developers': all_developers,
    }
    return HttpResponse(template.render(context, request))


def detail1(request, genres_id):
    try:
        genres = Genre.objects.get(pk=genres_id)
    except Genre.DoesNotExist:
        raise Http404("Album does not exist")

    template = loader.get_template('games/detail.html')
    context = {
        'genres': genres,
    }

    return HttpResponse(template.render(context, request))

def detail2(request, games_id):
    try:
        games = Game.objects.get(pk=games_id)
    except Genre.DoesNotExist:
        raise Http404("Album does not exist")

    template = loader.get_template('games/detail1.html')
    context = {
        'games': games,
    }

    return HttpResponse(template.render(context, request))


def detail3(request, developers_id):
    try:
        developers = Developer.objects.get(pk=developers_id)
    except Genre.DoesNotExist:
        raise Http404("Album does not exist")

    template = loader.get_template('games/detail2.html')
    context = {
        'developers': developers,
    }

    return HttpResponse(template.render(context, request))
