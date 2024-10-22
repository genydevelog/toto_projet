"""
URL configuration for toto_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from toto_app import views  # Importation des vues de l'application Toto

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'admin Django
    path('', include('toto_app.urls')),  # Page d'accueil pour afficher les enregistrements
    # path('record/new/', views.record_create, name='record_create'),  # URL pour créer un nouvel enregistrement
    # path('record/<int:id>/edit/', views.record_update, name='record_update'),  # URL pour modifier un enregistrement
    # path('record/<int:id>/delete/', views.record_delete, name='record_delete'),  # URL pour supprimer un enregistrement
]
