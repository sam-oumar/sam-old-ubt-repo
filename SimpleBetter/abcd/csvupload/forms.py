import io
import csv
from django import forms

class DataForm(forms.form):
	data_file = forms.FileField()

	def process_data(self):
		