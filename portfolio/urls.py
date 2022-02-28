from django.urls import path
from .views import home_page, about_page, contact_page, projects_page, projects_detail_page


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('projects/', projects_page, name='projects'),
    path('projects/<int:project_id>',
         projects_detail_page, name='projects-detail'),
]
