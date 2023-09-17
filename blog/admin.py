from django.contrib import admin
from .models import Articles, Abonne, Utilisateur

# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display=('name', 'description', 'like', 'image')


admin.site.register(Articles, AdminArticle)
admin.site.register(Abonne)
admin.site.register(Utilisateur)