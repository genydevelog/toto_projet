// scripts.js

// Fonction pour afficher une alerte de confirmation avant de supprimer un enregistrement
function confirmDelete(event) {
    if (!confirm("Êtes-vous sûr de vouloir supprimer cet enregistrement ?")) {
        event.preventDefault();  // Annule l'action si l'utilisateur ne confirme pas
    }
}

// Ajout d'un écouteur d'événements à tous les liens de suppression
document.querySelectorAll('.delete-link').forEach(link => {
    link.addEventListener('click', confirmDelete);  // Appelle la fonction de confirmation lors du clic
});