from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    subcategories = Subcategory.objects.filter(category=category)
    context = {
        'category': category,
        'subcategories': subcategories,
    }
    return render(request, 'main/category-page.html', context)


def subcategories(request, category_slug, subcategory_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug, category=category)
    articles = Article.objects.filter(subcategory=subcategory)
    context = {
        'subcategory': subcategory,
        'articles': articles,
    }
    return render(request, 'main/subcategory.html', context)


def article_page(request, category_slug, subcategory_slug, article_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(Subcategory, slug=article_slug)
    article = Article.objects.get(slug=subcategory_slug)
    context = {
        'subcategory': subcategory,
        'article': article,
    }
    return render(request, 'main/subcategory.html', context)