"""
Exercice 3 : vérificateur de sudoku
===================================

Une grille de sudoku est une liste de 9 lignes, chaque ligne étant une
liste de 9 entiers. On accède à une case avec grille[ligne][colonne].

Complétez les fonctions ci-dessous DANS L'ORDRE, en remplaçant `pass`
par votre code. Chaque fonction peut (et doit) utiliser les précédentes.

Règles :
    - Ne modifiez PAS le nom des fonctions ni leurs paramètres.
    - N'utilisez PAS set() ni sorted() : le but est d'écrire l'algorithme
      vous-même avec des boucles.
    - Ne modifiez pas la grille reçue.

Lancez les tests avec :  pytest test_exercise.py -v
"""


# ---------------------------------------------------------------------------
# Étape 1 : vérifier un groupe de 9 cases
# ---------------------------------------------------------------------------
def groupe_valide(groupe):
    """
    Retourne True si `groupe` (list) contient exactement les nombres de
    1 à 9, chacun une seule fois (dans n'importe quel ordre), sinon False.

    Retourne False si :
        - le groupe n'a pas exactement 9 éléments,
        - un élément n'est pas un int (ou est un bool),
        - un élément n'est pas entre 1 et 9,
        - un nombre apparaît deux fois.

    Astuce : une liste `deja_vu = [False] * 10` permet de retenir les
    nombres déjà rencontrés (deja_vu[5] passe à True quand on voit un 5).

    Exemples :
        >>> groupe_valide([5, 3, 4, 6, 7, 8, 9, 1, 2])
        True
        >>> groupe_valide([5, 3, 4, 6, 7, 8, 9, 1, 5])
        False
        >>> groupe_valide([1, 2, 3])
        False
    """
    pass


# ---------------------------------------------------------------------------
# Étape 2 : les lignes
# ---------------------------------------------------------------------------
def lignes_valides(grille):
    """
    Retourne True si les 9 lignes de la grille sont valides, sinon False.

    Exemple :
        >>> lignes_valides(GRILLE_VALIDE)
        True
        >>> lignes_valides(GRILLE_LIGNE_FAUSSE)
        False
    """
    pass


# ---------------------------------------------------------------------------
# Étape 3 : les colonnes (boucle dans une boucle)
# ---------------------------------------------------------------------------
def colonnes_valides(grille):
    """
    Retourne True si les 9 colonnes de la grille sont valides, sinon False.

    Pour chaque colonne, construisez une liste avec la case de cette
    colonne dans chacune des 9 lignes, puis vérifiez-la.

    Exemple :
        >>> colonnes_valides(GRILLE_VALIDE)
        True
        >>> colonnes_valides(GRILLE_COLONNE_FAUSSE)
        False
    """
    pass


# ---------------------------------------------------------------------------
# Étape 4 : les carrés 3x3 (boucles imbriquées)
# ---------------------------------------------------------------------------
def carres_valides(grille):
    """
    Retourne True si les 9 carrés 3x3 de la grille sont valides, sinon False.

    Les carrés commencent aux lignes 0, 3, 6 et aux colonnes 0, 3, 6.
    Pour chaque carré, rassemblez ses 9 cases dans une liste, puis
    vérifiez-la.

    Exemple :
        >>> carres_valides(GRILLE_VALIDE)
        True
        >>> carres_valides(GRILLE_CARRE_FAUSSE)
        False
    """
    pass


# ---------------------------------------------------------------------------
# Étape 5 : la grille complète
# ---------------------------------------------------------------------------
def sudoku_valide(grille):
    """
    Retourne True si la grille est un sudoku résolu correct, sinon False.

    1. Vérifiez d'abord le FORMAT : `grille` doit être une list de 9
       éléments, et chaque ligne une list de 9 éléments.
       Si ce n'est pas le cas, retournez False (sans planter).
    2. Puis vérifiez les lignes, les colonnes et les carrés.

    Exemples :
        >>> sudoku_valide(GRILLE_VALIDE)
        True
        >>> sudoku_valide(GRILLE_CARRE_FAUSSE)
        False
        >>> sudoku_valide([[1, 2, 3]])
        False
    """
    pass
