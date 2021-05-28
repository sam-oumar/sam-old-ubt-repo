from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Company, Employees, Question, Reponse, Author
from django.views.generic import (CreateView, DeleteView, DetailView,  ListView, UpdateView, TemplateView)
from .forms import FormCreatePerson, FormCreateQuestion, FormCreateReponse
from django.forms import modelformset_factory

# Create your views here.
class HomeView(TemplateView):
    template_name = "clbaseviews/home.html"

class PersonListView(ListView):
    model = Person
    template_name = "clbaseviews/list_person.html"

class PersonCreateView(CreateView):
    model = Person
    form_class = FormCreatePerson
    template_name = "clbaseviews/create_person.html"

class PersonDetailView(DetailView):
    model = Person
    template_name = "clbaseviews/detail_person.html"


class EmployeesListView(ListView):
    model = Company
    context_objects_name = 'company'
    template_name = 'clbaseviews/employee_list.html'

    # def get_queryset(self):
    #     return Company.objects.filter(pk=self.kwargs["pk"])

employee_listview = EmployeesListView.as_view()

class EmployeesDetailView(DetailView):
	model = Employees
	# context_objects_name = 'employee'
	template_name = 'clbaseviews/employee_detail.html'

employee_detailview = EmployeesDetailView.as_view()

def question(request):
    if request.method == "POST":
        form=FormCreateQuestion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clbaseviews:liste_question')
    
    form=FormCreateQuestion()
    return render(request, 'clbaseviews/question.html', {'form': form})

def reponse(request, slug):
    post = get_object_or_404(Question, slug=slug)
    print("+++++++++++++++++++++++++++++++++++", post)
    if request.method == "POST":
        form=FormCreateReponse(request.POST)
        if form.is_valid():
            rep = form.save(commit=False)
            rep.question = post
            rep.save()
            return redirect('clbaseviews:liste_question')
    else:
        form=FormCreateReponse()
        frm = post
        context = {"form": form, "frm": frm}
    return render(request, 'clbaseviews/reponse.html', context)

# def liste_question(request):
#     question = Question.objects.all()
#     return render(request, 'clbaseviews/liste_question.html', {"question": question})

class QuestionListView(ListView):
    model = Question
    template_name = "clbaseviews/liste_question.html"
    context_objects_name = "question"

# def Author(request):
#     AuthorFormSet = modelformset_factory(Author, fields=('name', 'email'))
#     form = AuthorFormSet()
    
#     return render(request, "clbaseviews/author.html", {"form": form} )