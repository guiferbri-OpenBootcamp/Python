from django.shortcuts import render
from .models import Director, Movie


# Create your views here.
def index(request):
    num_directors = Director.objects.all().count()
    directors = Director.objects.all()

    return render(
        request,
        'director_list.html',
        context={
            'num_directors': num_directors,
            'directors': directors
        }
    )


def directordetail(request, id):
    director = Director.objects.get(pk=id)
    return render(
        request,
        'director_detail.html',
        context={
            'director': director
        }
    )

def moviedetail(request, id):
    movie = Movie.objects.get(pk=id)
    return render(
        request,
        'movie_detail.html',
        context={
            'movie': movie
        }
    )