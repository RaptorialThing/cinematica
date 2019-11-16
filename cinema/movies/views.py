from django.shortcuts import render
from movies.models import Movies

# Create your views here.


def movies_index(request):
	movies = Movies.objects.all()
	context = {
		'movies': movies
	}
	return render(request,'movies_index.html',context)

def movies_detail(request,pk):
	movies = Movies.objects.get(pk=pk)
	context = {
		'movies': movies
	}	
	return render(request,'movies_detail.html',context)

