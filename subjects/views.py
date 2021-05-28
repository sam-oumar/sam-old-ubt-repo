import csv, io
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView,  ListView, UpdateView, TemplateView)
from .models import Subject
from django.contrib import messages

# Create your views here.
class SubjectListView(ListView):
    model = Subject
    template_name = "subjects/subject_list.html"

    def get_queryset(self):
        return Subject.objects.filter(classroom=self.kwargs["serie"]).order_by("year")
    

class SubjectDetailView(DetailView):
    model = Subject




def UploadSubjectCsv(request):
    template = 'subjects/subject_upload.html'

    orders = {
        'Order': 'The Csv file must be ordered by year, duration, matiere, classroom, coefficient, page_count'}

    if request.method == 'GET':
        return render(request, template, orders)
    
    csv_file = request.FILES['subjects']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created=Subject.objects.update_or_create(
            year=column[0],
            # duration=column[1],
            matiere=column[1],
            # category = column[3],
            classroom=column[2],
            coefficient=column[3],
            page_count=column[4])
    context = {}
    return render(request, template, context)
