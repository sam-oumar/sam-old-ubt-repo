from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Crmessage, Crservice, Crimputation

class UserCreerForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		
class FormCrmessage(forms.ModelForm):
	class Meta:
		type_msg = (("DIRECTION","Direction"),("AUTRES","Autres"))
		model=Crmessage
		fields = ['designation','objet', 'date_courrier', 'date_reception','type_message']
		widgets= {
		'type_message':forms.Select(choices=type_msg),
		'date_courrier':forms.DateInput(attrs={"class": "input", "type": "date"}, format="%Y-%m-%d"),
		'date_reception':forms.DateInput(attrs={"class": "input", "type": "date"}, format="%Y-%m-%d"),
		# 'crmessage':forms.Select(attrs={'class': 'input'}),
		# 'crservice':forms.Select()
		 }

class FormCrservice(forms.ModelForm):
	class Meta:
		model=Crservice
		fields = ['code_srv','nom_service']

class FormCrimputation(forms.ModelForm):
	class Meta:
		msg = (("TRAITER","Traité"),("NONTRAITER","Non Traité"))
		model=Crimputation
		fields = ['date_imput','date_lmt_trmt', 'observation', 'statut_msg', 'crmessage', 'crservice']
		widgets= {
		'statut_msg':forms.Select(choices=msg),
		'date_imput':forms.DateInput(attrs={"class": "input", "type": "date"}, format="%Y-%m-%d"),
		'date_lmt_trmt':forms.DateInput(attrs={"class": "input", "type": "date"}, format="%Y-%m-%d"),
		# 'crmessage':forms.Select(attrs={'class': 'input'}),
		# 'crservice':forms.Select()
		 }