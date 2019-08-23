from django.urls import path
from .views import (ArticleListView, ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView
                    ,MyFbv, CourseView,CourseListView,MyListView,CourseCreateView,CourseUpdateView,CourseDeleteView)
from django.contrib.auth.decorators import login_required
app_name = 'article'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-details'),
    path('create/', ArticleCreateView.as_view(), name='articles-create'),
    path('<int:id>/update/', login_required(ArticleUpdateView.as_view()), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('myfbv/', MyFbv, name='MyFbv'),
    path('ctem/', CourseView.as_view(template_name='CBVExamples/contact.html'), name='Course-list'),
    path('clist/<int:id>/', CourseView.as_view(), name='Course-list'),
    path('clist/', CourseListView.as_view(), name='Course-list'),  #parameter template url
    path('mylist/', MyListView.as_view(), name='Course-list'),
    path('CourseCreate/', CourseCreateView.as_view(), name='Course-create'),  # default tempalte url
    path('<int:id>/Courseupdate/', CourseUpdateView.as_view(), name='Course-update'),
    path('<int:id>/Coursedelete/', CourseDeleteView.as_view(), name='Course-delete'),
     ]