from django.urls import path
from .views import projects_page, projects_detail_page


urlpatterns = [
    path('', projects_page, name='projects'),
    path('<int:project_id>', projects_detail_page, name='projects-detail'),
]
