from django.shortcuts import get_object_or_404, render

from projects.models import Project

# Create your views here.


def projects_page(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    template_name = 'projects/home.html'

    return render(request, template_name, context)


def projects_detail_page(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        'project': project,
    }
    template_name = 'projects/projects-detail.html'

    return render(request, template_name, context)
