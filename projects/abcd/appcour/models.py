import random
from django.db import models

# Create your models here.
class Crmessage(models.Model):
	code_msg = models.CharField(max_length=15)
	designation = models.CharField(max_length=300)
	objet = models.CharField(max_length=300)
	date_courrier = models.DateField()
	date_reception = models.DateField()
	type_message = models.CharField(max_length=100)
	usager_insert = models.CharField(max_length=100, null=True)
	# date_insert = models.DateTimeField(auto_now_add=True)
	date_insert = models.DateTimeField()
	usager_update = models.CharField(max_length=100, null=True)
	date_update = models.DateTimeField(auto_now=True)

	def _get_code_msg(self):
		return random.randint(1, 10000)

	def __str__(self):
		return self.designation

	def save(self, *args, **kwargs):
		if not self.code_msg:
			self.code_msg = "ME-"+str(self._get_code_msg())
		super().save(*args, **kwargs)


class Crservice(models.Model):
	code_srv = models.CharField(max_length=100)
	nom_service = models.CharField(max_length=100)

	def __str__(self):
		return self.code_srv

class Crimputation(models.Model):
	date_imput = models.DateField()
	date_lmt_trmt = models.DateField()
	observation = models.TextField(null=True, blank=True)
	statut_msg = models.CharField(max_length=15)
	usager_insert = models.CharField(max_length=100, null=True)
	# date_insert = models.DateTimeField(auto_now_add=True)
	date_insert = models.DateTimeField()
	usager_update = models.CharField(max_length=100, null=True)
	date_update = models.DateTimeField(auto_now=True)
	crservice = models.ForeignKey(Crservice, on_delete=models.CASCADE)
	crmessage = models.ForeignKey(Crmessage, on_delete=models.CASCADE)