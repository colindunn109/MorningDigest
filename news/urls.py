from django.urls import path,include
from . import views

app_name = 'news'

urlpatterns = [
    path('articlelist/',views.ArticleListView.as_view(),name="articlelist"),
    path('articlelist/<pk>',views.ArticleDetailView.as_view(),name="articledetail"),
]
