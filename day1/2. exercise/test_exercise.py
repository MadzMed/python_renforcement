"""
Tests de l'exercice 2.

Lancement :  pytest test_exercise.py -v
"""

import copy

import pytest

from donnees import ECOLE
from exercise import (
    acces_chemin,
    dernier_telephone,
    eleves_par_option,
    email_professeur,
    latitude_ecole,
    moyenne_eleve,
    prenoms_eleves,
    trouver_eleve,
    ville_ecole,
)

# Une deuxième structure, plus petite, pour vérifier que les réponses
# ne sont pas écrites « en dur ».
PETITE_ECOLE = {
    "nom": "Mini École",
    "adresse": {"ville": "Nantes", "code_postal": "44000", "coordonnees": (47.21, -1.55)},
    "classes": [
        {
            "nom": "Unique",
            "professeur": {
                "nom": "Petit",
                "contact": {"email": "petit@mini.fr", "telephones": ["01 02 03 04 05", "09 87 65 43 21"]},
            },
            "horaires": {"samedi": [("10:00", "11:00")]},
            "eleves": [
                {
                    "id": 42,
                    "prenom": "Zoé",
                    "age": 20,
                    "actif": True,
                    "notes": {"python": [20, 10, 13]},
                    "options": {"échecs"},
                    "tuteur": None,
                },
                {
                    "id": 43,
                    "prenom": "Yann",
                    "age": 23,
                    "actif": True,
                    "notes": {"python": [7]},
                    "options": {"échecs", "sport"},
                    "tuteur": None,
                },
            ],
        }
    ],
}

SANS_CLASSE = {
    "nom": "Vide",
    "adresse": {"ville": "Paris", "code_postal": "75000", "coordonnees": (48.85, 2.35)},
    "classes": [],
}


# ---------------------------------------------------------------------------
# Niveau 1 : accès direct
# ---------------------------------------------------------------------------
class TestNiveau1:
    def test_ville(self):
        assert ville_ecole(ECOLE) == "Lyon"

    def test_ville_autre_structure(self):
        assert ville_ecole(PETITE_ECOLE) == "Nantes"

    def test_latitude(self):
        assert latitude_ecole(ECOLE) == 45.76

    def test_latitude_autre_structure(self):
        assert latitude_ecole(PETITE_ECOLE) == 47.21

    @pytest.mark.parametrize(
        "index, attendu",
        [
            (0, "martin@academie-python.fr"),
            (1, "nguyen@academie-python.fr"),
            (2, "garcia@academie-python.fr"),
        ],
    )
    def test_email_professeur(self, index, attendu):
        assert email_professeur(ECOLE, index) == attendu

    def test_email_professeur_autre_structure(self):
        assert email_professeur(PETITE_ECOLE, 0) == "petit@mini.fr"

    @pytest.mark.parametrize(
        "index, attendu",
        [
            (0, "04 72 00 00 01"),
            (1, "06 98 76 54 32"),  # un seul numéro : c'est aussi le dernier
            (2, "07 44 55 66 77"),
        ],
    )
    def test_dernier_telephone(self, index, attendu):
        assert dernier_telephone(ECOLE, index) == attendu

    def test_dernier_telephone_autre_structure(self):
        assert dernier_telephone(PETITE_ECOLE, 0) == "09 87 65 43 21"


# ---------------------------------------------------------------------------
# Niveau 2 : parcourir la structure
# ---------------------------------------------------------------------------
class TestNiveau2:
    def test_prenoms(self):
        assert prenoms_eleves(ECOLE) == [
            "Alice", "Bilal", "Chloé", "David", "Emma", "Farid", "Gaëlle", "Hugo",
        ]

    def test_prenoms_autre_structure(self):
        assert prenoms_eleves(PETITE_ECOLE) == ["Zoé", "Yann"]

    def test_prenoms_sans_classe(self):
        assert prenoms_eleves(SANS_CLASSE) == []

    @pytest.mark.parametrize("id_eleve, prenom", [(1, "Alice"), (5, "Emma"), (8, "Hugo")])
    def test_trouver_eleve(self, id_eleve, prenom):
        eleve = trouver_eleve(ECOLE, id_eleve)
        assert isinstance(eleve, dict)
        assert eleve["id"] == id_eleve
        assert eleve["prenom"] == prenom

    def test_trouver_eleve_autre_structure(self):
        assert trouver_eleve(PETITE_ECOLE, 43)["prenom"] == "Yann"

    @pytest.mark.parametrize("id_eleve", [0, 99, -1])
    def test_trouver_eleve_inconnu(self, id_eleve):
        assert trouver_eleve(ECOLE, 1) is not None, "trouver_eleve n'est pas encore implémentée"
        assert trouver_eleve(ECOLE, id_eleve) is None

    @pytest.mark.parametrize(
        "prenom, matiere, attendu",
        [
            ("Alice", "python", 13.75),
            ("Alice", "sql", 9.0),
            ("Bilal", "python", 9.67),
            ("Emma", "sql", 11.75),
            ("Farid", "python", 18.83),
        ],
    )
    def test_moyenne(self, prenom, matiere, attendu):
        assert moyenne_eleve(ECOLE, prenom, matiere) == attendu

    def test_moyenne_autre_structure(self):
        assert moyenne_eleve(PETITE_ECOLE, "Zoé", "python") == 14.33

    @pytest.mark.parametrize(
        "prenom, matiere",
        [
            ("Bilal", "sql"),     # matière absente
            ("Chloé", "python"),  # liste de notes vide
            ("Gaëlle", "python"), # aucune note du tout
            ("Hugo", "sql"),      # liste de notes vide
            ("Inconnu", "python"),# élève absent
        ],
    )
    def test_moyenne_none(self, prenom, matiere):
        assert moyenne_eleve(ECOLE, "Alice", "python") is not None, "moyenne_eleve n'est pas encore implémentée"
        assert moyenne_eleve(ECOLE, prenom, matiere) is None


# ---------------------------------------------------------------------------
# Niveau 3 : accès sécurisé et regroupement
# ---------------------------------------------------------------------------
class TestNiveau3:
    def test_eleves_par_option(self):
        assert eleves_par_option(ECOLE) == {
            "sport": ["Alice", "David", "Farid"],
            "cantine": ["Alice", "Bilal", "Farid", "Gaëlle"],
            "théâtre": ["David", "Emma", "Farid"],
        }

    def test_eleves_par_option_autre_structure(self):
        assert eleves_par_option(PETITE_ECOLE) == {
            "échecs": ["Yann", "Zoé"],
            "sport": ["Yann"],
        }

    def test_eleves_par_option_sans_classe(self):
        assert eleves_par_option(SANS_CLASSE) == {}

    @pytest.mark.parametrize(
        "chemin, attendu",
        [
            (["nom"], "Académie Python"),
            (["classes", 0, "professeur", "nom"], "Martin"),
            (["adresse", "coordonnees", 1], 4.83),               # dans un tuple
            (["adresse", "coordonnees", -1], 4.83),              # index négatif
            (["classes", -1, "eleves", 0, "prenom"], "Farid"),
            (["classes", 0, "horaires", "lundi", 0, 1], "12:00"),
            (["classes", 1, "eleves", 1, "tuteur", "nom"], "Leroy"),
            (["classes", 2, "eleves", 0, "notes", "python", 2], 20),
        ],
    )
    def test_acces_chemin(self, chemin, attendu):
        assert acces_chemin(ECOLE, chemin) == attendu

    @pytest.mark.parametrize(
        "chemin",
        [
            ["adresse", "pays"],                               # clé absente
            ["classes", 10, "nom"],                            # index trop grand
            ["classes", -4],                                   # index négatif trop grand
            ["classes", "0"],                                  # str sur une liste
            ["adresse", 0],                                    # int sur un dict absent
            ["nom", 0],                                        # on ne descend pas dans un str
            ["classes", 0, "eleves", 0, "tuteur", "nom"],      # tuteur vaut None
            ["classes", 0, "eleves", 0, "age", "valeur"],      # on ne descend pas dans un int
        ],
    )
    def test_acces_chemin_impossible(self, chemin):
        assert acces_chemin(ECOLE, ["nom"]) is not None, "acces_chemin n'est pas encore implémentée"
        assert acces_chemin(ECOLE, chemin) is None

    def test_acces_chemin_vide(self):
        assert acces_chemin(ECOLE, []) is ECOLE

    def test_acces_chemin_autre_structure(self):
        assert acces_chemin(PETITE_ECOLE, ["classes", 0, "eleves", 1, "prenom"]) == "Yann"


# ---------------------------------------------------------------------------
# Les fonctions ne doivent pas modifier la structure
# ---------------------------------------------------------------------------
def test_structure_non_modifiee():
    assert prenoms_eleves(ECOLE) is not None, "Les fonctions ne sont pas encore implémentées"
    avant = copy.deepcopy(ECOLE)
    ville_ecole(ECOLE)
    latitude_ecole(ECOLE)
    email_professeur(ECOLE, 0)
    dernier_telephone(ECOLE, 0)
    prenoms_eleves(ECOLE)
    trouver_eleve(ECOLE, 1)
    moyenne_eleve(ECOLE, "Alice", "python")
    eleves_par_option(ECOLE)
    acces_chemin(ECOLE, ["classes", 0, "eleves"])
    assert ECOLE == avant, "La structure ECOLE a été modifiée !"
