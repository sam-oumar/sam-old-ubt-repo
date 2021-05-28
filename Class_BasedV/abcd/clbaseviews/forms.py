from django import forms
from .models import Person, Question, Reponse

class FormCreatePerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "address", "number"]

class FormCreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

class FormCreateReponse(forms.ModelForm):
    class Meta:
        model = Reponse
        # fields = "__all__"
        fields = ["contenu", "auteur"]
