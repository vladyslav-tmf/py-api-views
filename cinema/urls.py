from django.urls import path
from cinema import views


app_name = "cinema"

cinema_hall_list = views.CinemaHallViewSet.as_view(
    actions={"get": "list", "put": "create"}
)
cinema_hall_detail = views.CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("genres/", views.GenreList.as_view(), name="genre-list"),
    path(
        "genres/<int:pk>/",
        views.GenreDetail.as_view(),
        name="genre-detail"),
    path("actors/", views.ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", views.ActorDetail.as_view(), name="actor-detail"),
    path("cinema-halls/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinema-halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),
]
