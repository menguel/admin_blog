from django.urls import path
from blog.views import home, blog, detail, articleCreate, modifier, table, deleteArticle


urlpatterns = [
    path('home', home,name='home'),
    path('blog', blog, name='blog'),
    path('', detail, name='detail'),
    path('create', articleCreate, name='create'),
    path('update/<int:my_id>', modifier, name='update'),
    path('tables', table, name='tables'),
    path('delete/<int:my_id>', deleteArticle, name='deleteArticle')
]