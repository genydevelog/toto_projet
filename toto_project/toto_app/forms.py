from django import forms
from .models import Record  # Importation du modèle Record

# Formulaire pour le modèle Record
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record  # Spécifie le modèle à utiliser
        fields = ['title', 'description']  # Champs à inclure dans le formulaire