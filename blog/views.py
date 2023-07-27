from django.shortcuts import render, get_object_or_404 , redirect
from django.http import Http404
from django.http import HttpResponse
from .models import Articles
# Create your views here.
# MCV : Model Views Controller  MVT : Model Views Template
from .form import ArticleForm , RowArticleForm

def home(request, *args, **kwargs):
    name = 'joe elono'
    number = 55
    mylist = [9,10,12,13,21]
    context = {
        'nom' : name,
        'numero' :number,
        'maList': mylist

    }
    return render(request, 'index1.html', context)


def blog(request, *args, **kwargs):
    return HttpResponse('<h1> la page de blog </h1>')


def detail(request, *args, **kwargs):
    article = Articles.objects.all()
    context = {
        'article':article,
    }
    return render(request, 'articles/details.html', context)


def articleCreate(request):
    form = ArticleForm(request.POST or None)
    message =''
    if form.is_valid():
        form.save()
        form = ArticleForm()
        message = 'Your modification was scuccessfuly done!'
    return render(request, 'articles/create.html', {'form':form, 'message':message })


def modifier(request, my_id):
    # Modifier le dernier produits 
    # last = Articles.objects.all().count()
    # obj = Articles.objects.get(id=last)
    # try:
    #     obj = Articles.objects.get(id=my_id)
    # except Articles.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Articles, id=my_id)
    form = ArticleForm(request.POST or None, instance=obj)
    message =''
    if form.is_valid():
        form.save()
        form = ArticleForm()
        message = 'We have receive your Article'
    return render(request, 'articles/update.html', {'form':form, 'message':message })


def table(request):
    obj = Articles.objects.all()
    return render(request, 'articles/tables.html', {'obj': obj} )
# def articleCreate(request):
#     if request.method == "POST" :
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         like = request.POST.get('like')
#         image = request.POST.get('image')
#         new_article = Articles.objects.create(name=name, description=description, like= like, image = image)
#         new_article.save()
#         message = "Your products was saved successfully"
#     return render(request, 'articles/create.html',{'messsage':message })


# def articleCreate(request):
#     form = RowArticleForm()
#     message = ''
#     if request.method == "POST":
#         form = RowArticleForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             new = Articles.objects.create(**form.cleaned_data)
#             new.save()
#             form = RowArticleForm
#             message = 'Article was successfully saved'
#     return render(request, 'articles/create.html', {'form':form, 'message':message})

def deleteArticle(request, my_id):
    obj = get_object_or_404(Articles, id=my_id)
    name = obj.name
    if request.method == "POST":
        obj.delete()

        return redirect('tables')

    return render(request, 'articles/delete.html', {'name':name})