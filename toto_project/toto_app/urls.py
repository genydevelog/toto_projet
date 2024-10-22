from django.urls import path
from toto_app import views  # Importation des vues de l'application Toto

urlpatterns = [
    path('', views.record_list, name='record_list'),  # Page d'accueil pour afficher les enregistrements
    path('record/new/', views.record_create, name='record_create'),  # URL pour créer un nouvel enregistrement
    path('record/<int:id>/edit/', views.record_update, name='record_update'),  # URL pour modifier un enregistrement
    path('record/<int:id>/delete/', views.record_delete, name='record_delete'),  # URL pour supprimer un enregistrement
]