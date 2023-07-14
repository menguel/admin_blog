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

#Chaque fois qu'on apporte des modifications à la table 
# $ python manage.py makemigrations   $ python manage.py migrate