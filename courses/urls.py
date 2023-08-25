from django.urls import path
from courses.views import List_view, Detail_view, Create_view, Update_view, Delete_view
app_name = 'courses'
urlpatterns = [
    path('', List_view.as_view(), name='courses-list'), # On peut changer le template name
    path('des', List_view.as_view(template_name="courses/course_list_des.html"), name='courses-list-des'), # On peut changer le template name
    path('<int:pk>/detail', Detail_view.as_view(), name='courses-detail'),
    path('create', Create_view.as_view(), name='courses-create'),
    path('<int:pk>/update', Update_view.as_view(), name='courses-update' ),
    path('<int:pk>/delete', Delete_view.as_view(), name='courses-delete')
]