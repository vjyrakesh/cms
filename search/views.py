from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage

# Create your views here.

def search(request):
	query = request.GET['q']
	return render_to_response('search/search.html',{'query':query,'results':FlatPage.objects.filter(content__icontains=query)})

def hello(request):
	return HttpResponse("Hello, World")
