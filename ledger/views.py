from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('landing page')

def recipe_list(request):
    return HttpResponse('recipe list')

def recipe_1(request):
    return HttpResponse('recipe 1')

def recipe_2(request):
    return HttpResponse('recipe 2')