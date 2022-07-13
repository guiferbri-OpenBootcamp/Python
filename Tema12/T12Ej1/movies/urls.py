from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<id>', views.directordetail, name='director_detail'),
    path('movie/<id>', views.moviedetail, name='movie_detail')
]