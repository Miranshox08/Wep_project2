from django.urls import path
from crud.views import article_func, article_detail,article_edit

urlpatterns = [
    path('', article_func, name="article_func"),
    path('<slug>', article_detail, name='article_detail'),
    path('<slug>/edit', article_edit, name='article_edit'),
]