from django.forms import ModelForm
from clients.models import Complaint
import djhacker
from django import forms
from dal import autocomplete

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['client', 'description', 'status']

    djhacker.formfield(
        Complaint.client,
        forms.ModelChoiceField,
        widget=autocomplete.ModelSelect2(url='clients-autocomplete')
    )