from django.shortcuts import render
from .models import Guide, Category
from django.template.response import SimpleTemplateResponse


def index(request):
    all_guides = Guide.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'guides/index.html', {'all_guides': all_guides, 'all_categories': all_categories})


def guide(request):
    return SimpleTemplateResponse('guides/guide.html')


def create_guide(request):
    return SimpleTemplateResponse('guides/create_guide.html')