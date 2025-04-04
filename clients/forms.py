from django.forms import ModelForm
from clients.models import Complaint

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['client', 'date_filed', 'description', 'status']

