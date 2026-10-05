"""
Tests de l'exercice 3.

Lancement :  pytest test_exercise.py -v
"""

import copy

import pytest

from exercise import carres_valides, colonnes_valides, groupe_valide, lignes_valides, sudoku_valide
from grilles import (
    GRILLE_CARRE_FAUSSE,
    GRILLE_COLONNE_FAUSSE,
    GRILLE_LIGNE_FAUSSE,
    GRILLE_VALIDE,
)


def transposer(grille):
    return [[grille[l][c] for l in range(9)] for c in range(9)]


def renumeroter(grille):
    # 1 -> 2, 2 -> 3, ..., 9 -> 1 : une grille valide reste valide.
    return [[case % 9 + 1 for case in ligne] for ligne in grille]


def modifier(grille, ligne, colonne, valeur):
    copie = copy.deepcopy(grille)
    copie[ligne][colonne] = valeur
    return copie


# Deux autres grilles valides, pour vérifier que rien n'est écrit « en dur ».
GRILLE_TRANSPOSEE = transposer(GRILLE_VALIDE)
GRILLE_RENUMEROTEE = renumeroter(GRILLE_VALIDE)


# ---------------------------------------------------------------------------
# Étape 1 : groupe_valide
# ---------------------------------------------------------------------------
class TestGroupeValide:
    @pytest.mark.parametrize(
        "groupe",
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1],
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
        ],
    )
    def test_groupe_correct(self, groupe):
        assert groupe_valide(groupe) is True

    @pytest.mark.parametrize(
        "groupe",
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 5],     # doublon
            [1, 1, 1, 1, 1, 1, 1, 1, 1],     # que des doublons
            [0, 2, 3, 4, 5, 6, 7, 8, 9],     # 0 interdit
            [10, 2, 3, 4, 5, 6, 7, 8, 9],    # 10 interdit
            [-1, 2, 3, 4, 5, 6, 7, 8, 9],    # négatif interdit
            [1, 2, 3, 4, 5, 6, 7, 8],        # 8 éléments
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],  # 10 éléments
            [],                              # vide
            ["1", 2, 3, 4, 5, 6, 7, 8, 9],   # str
            [1.0, 2, 3, 4, 5, 6, 7, 8, 9],   # float
            [True, 2, 3, 4, 5, 6, 7, 8, 9],  # bool (True vaut 1 en Python !)
            [None, 2, 3, 4, 5, 6, 7, 8, 9],  # None
        ],
    )
    def test_groupe_incorrect(self, groupe):
        assert groupe_valide([1, 2, 3, 4, 5, 6, 7, 8, 9]) is True, "groupe_valide n'est pas encore implémentée"
        assert groupe_valide(groupe) is False

    def test_groupe_non_modifie(self):
        groupe = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert groupe_valide(groupe) is True
        assert groupe == [9, 8, 7, 6, 5, 4, 3, 2, 1]


# ---------------------------------------------------------------------------
# Étapes 2 à 4 : lignes, colonnes, carrés
# Chaque fonction ne vérifie QUE sa règle : une grille fausse sur une autre
# règle doit quand même retourner True.
# ---------------------------------------------------------------------------
GRILLES_CORRECTES = [GRILLE_VALIDE, GRILLE_TRANSPOSEE, GRILLE_RENUMEROTEE]


class TestLignesValides:
    @pytest.mark.parametrize("grille", GRILLES_CORRECTES)
    def test_grilles_correctes(self, grille):
        assert lignes_valides(grille) is True

    @pytest.mark.parametrize("grille", [GRILLE_COLONNE_FAUSSE, GRILLE_CARRE_FAUSSE])
    def test_autres_regles_ignorees(self, grille):
        assert lignes_valides(grille) is True

    def test_ligne_fausse(self):
        assert lignes_valides(GRILLE_VALIDE) is True, "lignes_valides n'est pas encore implémentée"
        assert lignes_valides(GRILLE_LIGNE_FAUSSE) is False

    def test_derniere_ligne_fausse(self):
        assert lignes_valides(GRILLE_VALIDE) is True, "lignes_valides n'est pas encore implémentée"
        assert lignes_valides(modifier(GRILLE_VALIDE, 8, 8, 1)) is False


class TestColonnesValides:
    @pytest.mark.parametrize("grille", GRILLES_CORRECTES)
    def test_grilles_correctes(self, grille):
        assert colonnes_valides(grille) is True

    @pytest.mark.parametrize("grille", [GRILLE_LIGNE_FAUSSE, GRILLE_CARRE_FAUSSE])
    def test_autres_regles_ignorees(self, grille):
        assert colonnes_valides(grille) is True

    def test_colonne_fausse(self):
        assert colonnes_valides(GRILLE_VALIDE) is True, "colonnes_valides n'est pas encore implémentée"
        assert colonnes_valides(GRILLE_COLONNE_FAUSSE) is False

    def test_colonne_fausse_transposee(self):
        # Une ligne fausse devient une colonne fausse une fois transposée.
        assert colonnes_valides(GRILLE_VALIDE) is True, "colonnes_valides n'est pas encore implémentée"
        assert colonnes_valides(transposer(GRILLE_LIGNE_FAUSSE)) is False


class TestCarresValides:
    @pytest.mark.parametrize("grille", GRILLES_CORRECTES)
    def test_grilles_correctes(self, grille):
        assert carres_valides(grille) is True

    @pytest.mark.parametrize("grille", [GRILLE_LIGNE_FAUSSE, GRILLE_COLONNE_FAUSSE])
    def test_autres_regles_ignorees(self, grille):
        assert carres_valides(grille) is True

    def test_carre_faux(self):
        assert carres_valides(GRILLE_VALIDE) is True, "carres_valides n'est pas encore implémentée"
        assert carres_valides(GRILLE_CARRE_FAUSSE) is False

    @pytest.mark.parametrize("ligne, colonne", [(0, 0), (4, 4), (8, 8), (2, 6), (6, 2)])
    def test_une_case_fausse_dans_un_carre(self, ligne, colonne):
        assert carres_valides(GRILLE_VALIDE) is True, "carres_valides n'est pas encore implémentée"
        mauvaise_valeur = GRILLE_VALIDE[ligne][colonne] % 9 + 1
        assert carres_valides(modifier(GRILLE_VALIDE, ligne, colonne, mauvaise_valeur)) is False


# ---------------------------------------------------------------------------
# Étape 5 : sudoku_valide
# ---------------------------------------------------------------------------
class TestSudokuValide:
    @pytest.mark.parametrize("grille", GRILLES_CORRECTES)
    def test_grilles_correctes(self, grille):
        assert sudoku_valide(grille) is True

    @pytest.mark.parametrize(
        "grille",
        [GRILLE_LIGNE_FAUSSE, GRILLE_COLONNE_FAUSSE, GRILLE_CARRE_FAUSSE],
    )
    def test_grilles_fausses(self, grille):
        assert sudoku_valide(GRILLE_VALIDE) is True, "sudoku_valide n'est pas encore implémentée"
        assert sudoku_valide(grille) is False

    @pytest.mark.parametrize(
        "valeur",
        [0, 10, "5", 5.0, None, True],
    )
    def test_case_invalide(self, valeur):
        assert sudoku_valide(GRILLE_VALIDE) is True, "sudoku_valide n'est pas encore implémentée"
        assert sudoku_valide(modifier(GRILLE_VALIDE, 4, 4, valeur)) is False

    @pytest.mark.parametrize(
        "grille",
        [
            [],                                  # grille vide
            GRILLE_VALIDE[:8],                   # 8 lignes
            GRILLE_VALIDE + [GRILLE_VALIDE[0]],  # 10 lignes
            [ligne[:8] for ligne in GRILLE_VALIDE],  # lignes de 8 cases
            GRILLE_VALIDE[:8] + [[1, 2, 3]],     # une ligne trop courte
            [[1, 2, 3]],
            None,
            "123456789",
            [None] * 9,                          # les lignes ne sont pas des listes
        ],
    )
    def test_format_invalide(self, grille):
        assert sudoku_valide(GRILLE_VALIDE) is True, "sudoku_valide n'est pas encore implémentée"
        assert sudoku_valide(grille) is False

    def test_grille_non_modifiee(self):
        avant = copy.deepcopy(GRILLE_VALIDE)
        assert sudoku_valide(GRILLE_VALIDE) is True
        assert GRILLE_VALIDE == avant, "La grille a été modifiée !"
