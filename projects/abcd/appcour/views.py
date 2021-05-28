from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import UserCreerForm, FormCrmessage, FormCrservice, FormCrimputation
from .models import Crmessage, Crimputation, Crservice
import datetime

# Create your views here.
def home(request):
	return render(request,'appcour/pages/home.html')

# NewUser pwd batiment55
# Seconduser pwd batiment66
def creerUser(request):
	if request.method == 'POST':
		form = UserCreerForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Compte créé pour {username} !')
			return redirect('appcour:home')
	else:
		form = UserCreerForm()
	return render(request, 'appcour/pages/creeruser.html', {'form': form})

@login_required
def crmessage(request):
	form=FormCrmessage(request.POST)
	if form.is_valid():
		form = form.save(commit=False)
		form.usager_insert = request.user
		form.date_insert = datetime.datetime.now()
		form.save()
		messages.success(request, f'Votre courrier a été enregistré avec succès !')
		return redirect('appcour:crconsultation')
	else:
		form=FormCrmessage()
	return render(request, 'appcour/pages/crmessage.html', {'form': form})

@login_required
def crservice(request):
	form=FormCrservice(request.POST)
	if form.is_valid():
		form.save()
		messages.success(request, f'Service créé avec succès !')
		return redirect('appcour:home')
	else:
		form=FormCrservice()
	return render(request, 'appcour/pages/crservice.html', {'form': form})

@login_required
def crimputation(request):
	form=FormCrimputation(request.POST)
	if form.is_valid():
		form = form.save(commit=False)
		form.usager_insert = request.user
		form.date_insert = datetime.datetime.now()
		form.save()
		messages.success(request, f'Imputation effectuée avec succès !')
		return redirect('appcour:crconsultation')
	else:
		form=FormCrimputation()
	return render(request, 'appcour/pages/crimputation.html', {'form': form})

@login_required
def crconsultation(request):
	form = Crmessage.objects.all()
	return render(request, 'appcour/pages/crconsultation.html', {'form': form})

@login_required
def crdetail(request, crmsgid):
	form = get_object_or_404(Crmessage, pk=crmsgid)
	return render(request, 'appcour/pages/crdetail.html', {'form': form})

@login_required
def creditermsg(request, crmsgid):
	post = get_object_or_404(Crmessage, pk=crmsgid)
	if request.method == 'POST':
		form=FormCrmessage(request.POST, instance=post)
		if form.is_valid():
			form = form.save(commit=False)
			# form.usager_update = request.user
			# form.date_update = datetime.datetime.now()
			form.save()
			messages.success(request, f'Mise à jour effectuée avec succès !')
			return redirect('appcour:crconsultation')
	else:
		form=FormCrmessage(instance=post)
	return render(request, 'appcour/pages/creditermsg.html', {'form': form})

@login_required
def crsupprimer(request, crmsgid):
	form = get_object_or_404(Crmessage, pk=crmsgid)
	if request.method == 'POST':
		form.delete()
		messages.success(request, f'Courrier supprimé avec succès !')
	# return render(request, 'appcour/pages/crconsultation.html', {'form': form})
		return redirect('appcour:crconsultation')
	return render(request, 'appcour/pages/crsupprimer.html', {'form': form})

class ServiceListView(ListView):
	context_object_name = "services"
	model = Crservice
	template_name = "appcour/pages/crservice_list.html"