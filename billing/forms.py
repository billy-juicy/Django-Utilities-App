from django import forms
from billing.models import Tariff

class CalculateForm(forms.Form):
    number_month = forms.IntegerField(label="Month", min_value=1, max_value=12, widget=forms.TextInput(attrs={"id": "input1" }))
    tariff_month = forms.ModelChoiceField(queryset=Tariff.objects.all(), label="Tariff", empty_label='Select a tariff', to_field_name='rate', widget=forms.Select(attrs={"id": "tariff-select" }))