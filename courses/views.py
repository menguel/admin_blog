from django.shortcuts import get_object_or_404, redirect, render
from .models import Courses
from .form import CourseForm
from django.views import View

# Create your views here.

class List_view(View):
    template_name = 'courses/course_list.html'
    def get(self, request, *args, **kwargs):
        queryset = Courses.objects.all()
        return render(request, self.template_name, { 'object_list':queryset} )
    

class Detail_view(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        id = self.kwargs.get('pk')
        context = {}
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            context['object'] = obj
            return render(request, self.template_name, context)
        

class Create_view(View):
    template_name = "courses/course_create.html"

    form = CourseForm()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form})
    # Creation de cours (envoyer des données au serveurs)
    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/courses')
        

# Modifier un article
class Update_view(View):
    template_name = "courses/course_update.html"
    # obtenir l'article par l'id
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            return obj
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        form = CourseForm(instance=obj)
        return render(request, self.template_name, {'form':form})
    
    #Poster les modifs dans le serveur

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = CourseForm(request.POST, instance=obj)

        if form.is_valid():  # Si le formulaire est valide (n'a aucun problème)
            form.save()
            return redirect('/courses')
        

# Supprimer un article
# Messge pour avertir la suppression --> get | La suppression elle même --> post 
class Delete_view(View):

    template_name = "courses/course_delete.html"
    # recupere l'article à l'aide du id
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            return obj
    
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, )
    
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()

        return redirect('/courses')