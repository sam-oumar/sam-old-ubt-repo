from django.urls import path
from .views import HomeView, MovieList, MovieDetail

app_name = "movies"

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("movie_list", MovieList.as_view(), name="movie_list"),
	path("movie_detail/<slug:slug>", MovieDetail.as_view(), name="movie_detail"),
]