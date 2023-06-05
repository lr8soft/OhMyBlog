from django.urls import path, include
from django.views.generic import TemplateView

from . import articleViews

urlpatterns = [
    path("create_new_article", articleViews.create_new_article),
    path("get_pagination_articles", articleViews.get_pagination_articles),
    path("delete_article", articleViews.delete_article),
    path("get_article_detail", articleViews.get_article_detail),
]