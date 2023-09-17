from django.db.models.query import QuerySet
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

# Create your models here.
class Articles(models.Model):
    name = models.CharField(max_length=150)
    like = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(default='default_image.jpg', upload_to='images/images', blank=True)
    slug = models.SlugField(null=True)
    actif = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.name

    # Construire des urls dynamique
    def get_absolute_url(self):
        # Nom de la fonctionne à appeler
        return reverse("update", kwargs={"my_id": self.pk})


class AbonneManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args,**kwargs)

class Abonne(models.Model):
    abonne = AbonneManager()
    name = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.name
    

class Utilisateur(AbstractUser):
    name = models.CharField(max_length=50, blank=True)

    class Type(models.TextChoices):
        STUDENT = 'STUDENT', 'student'
        TEACHER = 'TEACHER', 'teacher'
        DIRECTOR = 'DIRECTOR', 'director'
    type = models.CharField(max_length=50, choices=Type.choices, default=Type.STUDENT)

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Utilisateur.Type.STUDENT)
    
class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Utilisateur.Type.TEACHER)
    
class DirectorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Utilisateur.Type.DIRECTOR)

class Studet(Utilisateur):
    objects = StudentManager()
    class Meta:
        proxy = True

class Teacher(Utilisateur):
    objects = TeacherManager()
    class Meta:
        proxy = True

class Director(Utilisateur):
    DirectorManager
    class Meta:
        proxy = True
    

#Chaque fois qu'on apporte des modifications à la table 
# $ python manage.py makemigrations   $ python manage.py migrate

# Lorsque l'on fait un abstractUser il faut aller dans settings et préciser celà