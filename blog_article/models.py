from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Artblog(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    auteur = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    image = models.ImageField(default='default_image.jpg', upload_to='images/images', blank=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    #  get_absolute_url() est important pour les detail
    def get_absolute_url(self):
        return reverse("blog_article:article-detail", kwargs={"pk": self.pk})
    