"""
Exercice 2 : accéder aux données d'une structure complexe
=========================================================

La structure à explorer se trouve dans `donnees.py` (variable ECOLE).
Complétez les fonctions ci-dessous en remplaçant `pass` par votre code.

Règles :
    - Ne modifiez PAS le nom des fonctions ni leurs paramètres.
    - Utilisez toujours le paramètre `donnees`, jamais ECOLE directement :
      les tests utilisent aussi d'autres structures.
    - Ne modifiez pas la structure reçue (lecture seule).

Lancez les tests avec :  pytest test_exercise.py -v
"""


# ===========================================================================
# Niveau 1 : accès direct (clés et index)
# ===========================================================================
def ville_ecole(donnees):
    """
    Retourne la ville de l'école (str).

    Exemple :
        >>> ville_ecole(ECOLE)
        'Lyon'
    """
    pass


def latitude_ecole(donnees):
    """
    Retourne la latitude de l'école (float) : c'est le PREMIER élément
    du tuple "coordonnees" de l'adresse.

    Exemple :
        >>> latitude_ecole(ECOLE)
        45.76
    """
    pass


def email_professeur(donnees, index_classe):
    """
    Retourne l'email (str) du professeur de la classe située à la
    position `index_classe` dans la liste des classes.

    Exemples :
        >>> email_professeur(ECOLE, 0)
        'martin@academie-python.fr'
        >>> email_professeur(ECOLE, 2)
        'garcia@academie-python.fr'
    """
    pass


def dernier_telephone(donnees, index_classe):
    """
    Retourne le DERNIER numéro de téléphone (str) du professeur de la
    classe située à la position `index_classe`.

    Exemples :
        >>> dernier_telephone(ECOLE, 0)
        '04 72 00 00 01'
        >>> dernier_telephone(ECOLE, 1)
        '06 98 76 54 32'
    """
    pass


# ===========================================================================
# Niveau 2 : parcourir la structure (boucles)
# ===========================================================================
def prenoms_eleves(donnees):
    """
    Retourne la liste (list) des prénoms de TOUS les élèves de l'école,
    classe après classe, dans l'ordre où ils apparaissent.

    Exemple :
        >>> prenoms_eleves(ECOLE)
        ['Alice', 'Bilal', 'Chloé', 'David', 'Emma', 'Farid', 'Gaëlle', 'Hugo']
    """
    pass


def trouver_eleve(donnees, id_eleve):
    """
    Retourne le dictionnaire (dict) de l'élève dont l'"id" vaut `id_eleve`.
    Retourne None si aucun élève n'a cet id.

    Exemples :
        >>> trouver_eleve(ECOLE, 5)["prenom"]
        'Emma'
        >>> trouver_eleve(ECOLE, 99)
        None
    """
    pass


def moyenne_eleve(donnees, prenom, matiere):
    """
    Retourne la moyenne (float, arrondie à 2 décimales) des notes de
    l'élève `prenom` dans la matière `matiere`.

    Retourne None si :
        - aucun élève ne porte ce prénom,
        - l'élève n'a pas cette matière dans ses notes,
        - la liste de notes de cette matière est vide.

    Exemples :
        >>> moyenne_eleve(ECOLE, "Alice", "python")
        13.75
        >>> moyenne_eleve(ECOLE, "Bilal", "sql")
        None
        >>> moyenne_eleve(ECOLE, "Chloé", "python")
        None
    """
    pass


# ===========================================================================
# Niveau 3 : accès sécurisé et regroupement
# ===========================================================================
def eleves_par_option(donnees):
    """
    Regroupe les élèves par option.

    Retourne un dictionnaire (dict) dont :
        - les clés sont les options (str),
        - les valeurs sont les listes des prénoms des élèves qui ont
          cette option, TRIÉES par ordre alphabétique.

    Une option que personne n'a choisie n'apparaît pas.

    Exemple :
        >>> eleves_par_option(ECOLE)
        {'sport': ['Alice', 'David', 'Farid'],
         'cantine': ['Alice', 'Bilal', 'Farid', 'Gaëlle'],
         'théâtre': ['David', 'Emma', 'Farid']}
        (l'ordre des clés n'a pas d'importance)
    """
    pass


def acces_chemin(donnees, chemin):
    """
    Suit un chemin (list) de clés et d'index dans la structure et retourne
    la valeur trouvée au bout.

    - Si l'élément courant est un dict, l'étape est une clé.
    - Si l'élément courant est une list ou un tuple, l'étape est un index
      (int, les index négatifs sont autorisés).
    - Si une étape est impossible (clé absente, index hors limites,
      mauvais type d'étape, ou élément qui n'est ni dict, ni list,
      ni tuple), retourne None.
    - Un chemin vide retourne `donnees` lui-même.

    Pas besoin de try/except : utilisez `in`, `len()` et `isinstance()`.

    Exemples :
        >>> acces_chemin(ECOLE, ["classes", 0, "professeur", "nom"])
        'Martin'
        >>> acces_chemin(ECOLE, ["adresse", "coordonnees", -1])
        4.83
        >>> acces_chemin(ECOLE, ["classes", 10, "nom"])
        None
        >>> acces_chemin(ECOLE, ["adresse", "pays"])
        None
    """
    pass
