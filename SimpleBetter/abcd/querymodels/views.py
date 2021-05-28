from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book

# Create your views here.
def home(request):
	return render(request, 'querymodels/home.html')

class PublisherList(ListView):
	model = Publisher
	context_object_name = 'publishers'

class PublisherDetail(DetailView):
	model = Publisher

	def get_context_data(self, **kwargs):
		context = super(PublisherDetail, self).get_context_data(**kwargs)
		context["book_list"] = Book.books.all()
		return context