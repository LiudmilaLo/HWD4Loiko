from django.urls import path
from .views import *


urlpatterns = [
    path('authorlist/', AuthorList.as_view()),
    path('news/', PostList.as_view()),
    path('news/<int:pk>/', PostOne.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view()),
    path('add/', PostCreateView.as_view(), name='post_add'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),

]
