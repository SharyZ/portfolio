from django.shortcuts import render

from projects.models import Project

# Create your views here.


def home_page(request):
    # last_projects = Project.objects.all()[:3]
    last_projects = Project.objects.order_by('-id')[:3]

    context = {
        'last_projects': last_projects,
    }
    template_name = 'portfolio/home.html'

    return render(request, template_name, context)


def about_page(request):
    context = {}
    template_name = 'portfolio/about.html'

    return render(request, template_name, context)


def contact_page(request):
    context = {}
    template_name = 'portfolio/contact.html'

    return render(request, template_name, context)
