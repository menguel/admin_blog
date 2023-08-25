from django.contrib import admin
from .models import Courses, Framework, Language, Profile

# Register your models here.

admin.site.register(Courses)
admin.site.register(Framework)
admin.site.register(Language)
admin.site.register(Profile)