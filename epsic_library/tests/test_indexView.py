import pytest
from django.test import Client
from django.urls import reverse

# Objectif du test : tester le comportement de la view index dans des conditions normales d'utlisation
@pytest.mark.django_db
def test_index_view():
    # Création d'un client de test pour simuler les requêtes HTTP vers les vues
    client = Client()
    # Envoi d'une requête GET à la vue 'index'
    response = client.get(reverse('index'))

    # Vérification du code de statut de la réponse (200 indique une réponse réussie)
    assert response.status_code == 200
    # Vérification que le template 'index.html' est utilisé pour rendre la réponse
    assert 'index.html' in [template.name for template in response.templates]

    context = response.context
    num_visits = context['num_visits']

    # (visite initiale)
    assert num_visits == 1

    #incrémentée après la requête
    assert client.session.get('num_visits') == 2  # Incrémentée après la requête
