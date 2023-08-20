from django.urls import path
from blog_article.views import ArticleLisView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'blog_article'
urlpatterns = [
    path('', ArticleLisView.as_view(), name='article-list'),
    path('<int:pk>/detail', ArticleDetailView.as_view(), name='article-detail'),
    path('create', ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='article-update' ),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete') # On peut aussi utiliser le slug pour deferencier eg : <slug:slug>
]
 