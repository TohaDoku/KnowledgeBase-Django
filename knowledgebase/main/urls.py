from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/', category_page, name='category_page'),
    path('category/<slug:category_slug>/<slug:subcategory_slug>/', subcategories, name='subcategory_detail'),
    path('category/<slug:category_slug>/<slug:subcategory_slug>/<slug:article_slug>/', article_page, name='article_page'),
]
