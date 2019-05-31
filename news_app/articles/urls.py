from django.urls import path
from .views import ArticleListView, DetailedArticle, EditArticle, DeleteArticle, CreateArticle


urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('<int:pk>/edit/', EditArticle.as_view(), name='article_edit'),
    path('<int:pk>/', DetailedArticle.as_view(), name='article_detail'),
    path('new/', CreateArticle.as_view(), name='article_create'),
    path('<int:pk>/delete/', DeleteArticle.as_view(), name='article_delete'),
]
