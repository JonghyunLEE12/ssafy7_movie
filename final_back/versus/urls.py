from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_id>/', views.article),
    path('articles/<int:article_id>/comments/', views.comment_create),
    path('articles/<int:article_id>/comments/<int:comment_id>/', views.comment),
]