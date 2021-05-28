from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView,  ListView, UpdateView, TemplateView)
from .models import Movies, MovieLinks

# Create your views here.
class HomeView(TemplateView):
    template_name = "movies/home.html"

class MovieList(ListView):
	model = Movies
	template_name = "movies/movie_list.html"

	def get_queryset(self):
		return Movies.objects.order_by("title")

class MovieDetail(DetailView):
	model = Movies
	template_name = "movies/movie_detail.html"

	def get_object(self):
		objects = super(MovieDetail, self).get_object()
		objects.views_count += 1
		objects.save()
		return objects

	def get_context_data(self, **kwargs):
		context = super(MovieDetail, self).get_context_data(**kwargs)
		context["links"] = MovieLinks.objects.filter(movie=self.get_object())
		return context