from django.urls import path
from . import views


urlpatterns = [
    path("", views.show_main, name = "main_page"),
    path("genre/<str:genre>", views.show_genres, name = "genre_page" ),
    path("books/<str:title>", views.show_reviews, name = "review_page"),
]


