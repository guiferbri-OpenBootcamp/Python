from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    summary = models.TextField(max_length=200)
    #duration = models.PositiveIntegerField()
    def __str__(self):
        return "Título: {}. Año: {}. Sinopsis: {}".format(self.title, self.year, self.summary)


class Director(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=80)
    birthdate = models.DateField()
    deathdate = models.DateField(null=True, blank=True)
    #biography = models.TextField()
    #image = models.URLField()

    def __str__(self):
        if self.deathdate is not None:
            return "Nombre: {} {}. ({} - {})".format(self.name, self.lastname, self.birthdate, self.deathdate)
        else:
            return "Nombre: {} {}. ({})".format(self.name, self.lastname, self.birthdate)
