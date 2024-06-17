from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

def movies(request):
    movie_objects = Movies.objects.all()                    #get all objects 
    
    movie_name = request.GET.get("movie_name")              #gets the movie name 
    
    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)                    #filter movie by movie name 
        
        
    paginator = Paginator(movie_objects, 2)                     #set pragnators instance    
    page_number = request.GET.get('page')                       # gets the number of the page 
    movie_list = paginator.get_page(page_number)                #get specific page from paginator
    
    return render(request, "newapp/movies.html", {'movie_list': movie_list, "movie_objects":movie_objects})
