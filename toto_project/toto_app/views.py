from django.shortcuts import render, redirect, get_object_or_404
from .models import Record  # Importation du modèle Record
from .forms import RecordForm  # Importation du formulaire pour les enregistrements

# Vue pour afficher la liste des enregistrements
def record_list(request):
    records = Record.objects.all()  # Récupération de tous les enregistrements
    return render(request, 'record_list.html', {'records': records})  # Rendu du template avec les enregistrements

# Vue pour créer un nouvel enregistrement
def record_create(request):
    if request.method == 'POST':  # Si la requête est de type POST
        form = RecordForm(request.POST)  # Créer un formulaire avec les données POST
        if form.is_valid():  # Vérifier si le formulaire est valide
            form.save()  # Enregistrer l'enregistrement dans la base de données
            return redirect('record_list')  # Rediriger vers la liste des enregistrements
    else:
        form = RecordForm()  # Créer un formulaire vide
    return render(request, 'record_form.html', {'form': form})  # Rendu du template avec le formulaire

# Vue pour mettre à jour un enregistrement existant
def record_update(request, id):
    record = get_object_or_404(Record, id=id)  #
     # Récupération de l'enregistrement ou 404 si non trouvé
    if request.method == 'POST':  # Si la requête est de type POST
        form = RecordForm(request.POST, instance=record)  # Créer un formulaire avec les données POST
        if form.is_valid():  # Vérifier si le formulaire est valide
            form.save()  # Enregistrer les modifications de l'enregistrement dans la base de données
            return redirect('record_list')  # Rediriger vers la liste des enregistrements
    else:
        form = RecordForm(instance=record)  # Créer un formulaire avec l'enregistrement existant
    return render(request, 'record_form.html', {'form': form})  # Rendu du template avec le formulaire

# Vue pour supprimer un enregistrement
def record_delete(request, id):
    record = get_object_or_404(Record, id=id)  # Récupération de l'enregistrement ou 404 si non trouvé
    if request.method == 'POST':  # Si la requête est de type POST
        record.delete()  # Supprimer l'enregistrement de la base de données
        return redirect('record_list')  # Rediriger vers la liste des enregistrements
    return render(request, 'record_confirm_delete.html', {'record': record})  # Rendu du template de confirmation de suppression
