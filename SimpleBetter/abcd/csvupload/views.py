import csv, io
from django.shortcuts import render
from django.contrib.messages import constants as messages
from .models import Contact
# Create your views here.

def contact_upload(request):
	template = 'csvupload/contact_upload.html'
	prompt = {
		'order': 'Order of the Csv shuold be first_name, last_name, email, message'
	}
	if request.method == 'GET':
		return render(request, template, prompt)

	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, created = Contact.objects.update_or_create(
			first_name = column[0],
			last_name = column[1],
			email = column[2],
			message = column[3],
		)

	context = {}
	return render(request, template, context)