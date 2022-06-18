from django.urls import path
from . import views

urlpatterns = [
    path('today/recommend/', views.recommend_today_movie),
    path('recommend/random/', views.recoomend_random_movie),
    path('<int:movie_id>/detail/', views.movie_detail),
    path('recommend/<str:keyword>/', views.keyword_recommend),
    path('<int:movie_id>/reviews/', views.create_review),
    path('reviews/<int:review_id>/', views.review),
]