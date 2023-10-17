from django import forms
from .models import contacts
from .models import portfolio
class contactForms(forms.ModelForm):
    class Meta:
        model = contacts
        fields = ['cont_name', 'cont_email', 'cont_message']

class portForms(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = ['port_name', 'port_desc', 'port_imag']