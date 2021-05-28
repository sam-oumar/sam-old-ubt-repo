from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import AddressForm

class HomeView(TemplateView):
	template_name = 'abcd/home.html'

def AddressCreateView(request):
	if request.method == 'POST':
		form = AddressForm(request.POST)
		if form.is_valid():
			contact_data = form.cleaned_data
	form = AddressForm()
	return render(request, 'abcd/forms.html', {'form':form})