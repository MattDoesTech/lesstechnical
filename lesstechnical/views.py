from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('Welcome to LessTechnical.com, nontechnical explanations of technical stuff') 
