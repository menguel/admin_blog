from django.contrib import admin
from .models import Articles

# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display=('name', 'description', 'like', 'image')


admin.site.register(Articles, AdminArticle)