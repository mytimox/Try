from django import forms
from landing.models import PIB

class PIBForm(forms.ModelForm):
    class Meta:
        model = PIB
        fields = ('first_name', 'last_name', 'email')