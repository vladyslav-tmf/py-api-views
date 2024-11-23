from django.urls import path
from cinema import views


app_name = "cinema"

urlpatterns = [
    path("genres/", views.GenreList.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        views.GenreDetail.as_view(),
        name="genre-detail"),
    path("actors/", views.ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", views.ActorDetail.as_view(), name="actor-detail")
]
