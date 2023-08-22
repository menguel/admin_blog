from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = ('Course')
        verbose_name_plural = ('Courses')


    def __str__(self) -> str:
        return self.title