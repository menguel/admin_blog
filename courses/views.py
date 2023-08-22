from django.shortcuts import render
from .models import Courses
from .form import CourseForm
from django.views import View

# Create your views here.

class List_view(View):
    template_name = 'courses/course_list.html'
    def get(self, request, *args, **kwargs):
        queryset = Courses.objects.all()
        return render(request, self.template_name, { 'object_list':queryset} )