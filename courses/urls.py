from django.urls import path
from courses.views import List_view
app_name = 'courses'
urlpatterns = [
    path('', List_view.as_view(), name='courses-list'), # On peut changer le template name
    path('des', List_view.as_view(template_name="courses/course_list_des.html"), name='courses-list-des'), # On peut changer le template name
    # path('<int:pk>/detail', ArticleDetailView.as_view(), name='article-detail'),
    # path('create', ArticleCreateView.as_view(), name='article-create'),
    # path('<int:pk>/update', ArticleUpdateView.as_view(), name='article-update' ),
    # path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete') 
]
 