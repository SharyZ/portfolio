from django.shortcuts import render

# Create your views here.


def home_page(request):
    context = {}
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


def projects_page(request):
    context = {}
    template_name = 'portfolio/projects.html'

    return render(request, template_name, context)


def projects_detail_page(request, project_id):
    context = {}
    template_name = 'portfolio/projects_detail.html'

    return render(request, template_name, context)
