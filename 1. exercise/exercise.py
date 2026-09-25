"""
Exercice 1 : conditions et boucles
==================================

Complétez les trois fonctions ci-dessous en remplaçant `pass` par votre code.
Ne modifiez PAS le nom des fonctions ni leurs paramètres : les tests en dépendent.

Lancez les tests avec :  pytest test_exercise.py -v
"""


# ---------------------------------------------------------------------------
# Partie 1 : les conditions (if / elif / else)
# ---------------------------------------------------------------------------
def categoriser_temperature(temperature):
    """
    Retourne une catégorie (str) selon la température reçue (int ou float).

    Règles :
        - temperature < 0          -> "glacial"
        - 0  <= temperature < 15   -> "froid"
        - 15 <= temperature < 25   -> "doux"
        - temperature >= 25        -> "chaud"
        - si temperature n'est pas un int ou un float -> "invalide"
          (attention : True et False ne sont PAS des températures valides)

    Exemples :
        >>> categoriser_temperature(-5)
        'glacial'
        >>> categoriser_temperature(15)
        'doux'
        >>> categoriser_temperature(30.5)
        'chaud'
        >>> categoriser_temperature("20")
        'invalide'
    """
    pass


# ---------------------------------------------------------------------------
# Partie 2 : les boucles (for)
# ---------------------------------------------------------------------------
def compter_voyelles(texte):
    """
    Compte le nombre de chaque voyelle dans un texte (str).

    Règles :
        - Retourne un dictionnaire avec TOUJOURS les 6 clés :
          "a", "e", "i", "o", "u", "y"
        - Les majuscules comptent comme des minuscules ("A" compte pour "a")
        - Les lettres accentuées (é, è, à...) ne sont PAS comptées
        - Un texte vide retourne un dictionnaire avec toutes les valeurs à 0

    Exemples :
        >>> compter_voyelles("Bonjour")
        {'a': 0, 'e': 0, 'i': 0, 'o': 2, 'u': 1, 'y': 0}
        >>> compter_voyelles("")
        {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
    """
    pass


# ---------------------------------------------------------------------------
# Partie 3 : boucles + conditions
# ---------------------------------------------------------------------------
def analyser_notes(notes):
    """
    Analyse une liste de notes (list) et retourne un bilan (dict).

    Règles :
        - Une note valide est un int ou un float (pas un bool) compris
          entre 0 et 20 inclus. Les autres valeurs sont IGNORÉES.
        - Le dictionnaire retourné contient les clés :
            "moyenne"   : moyenne des notes valides, arrondie à 2 décimales
            "admis"     : nombre de notes >= 10
            "recales"   : nombre de notes < 10
            "meilleure" : la note la plus haute
            "mention"   : selon la moyenne
                            >= 16 -> "Très bien"
                            >= 14 -> "Bien"
                            >= 12 -> "Assez bien"
                            >= 10 -> "Passable"
                            sinon -> "Insuffisant"
        - S'il n'y a aucune note valide, retourner :
            {"moyenne": 0.0, "admis": 0, "recales": 0,
             "meilleure": None, "mention": "Aucune note"}

    Contrainte : n'utilisez pas sum(), max(), ni len() sur la liste
    des notes valides — faites les calculs vous-même dans la boucle.

    Exemples :
        >>> analyser_notes([12, 8, 15.5])
        {'moyenne': 11.83, 'admis': 2, 'recales': 1, 'meilleure': 15.5, 'mention': 'Passable'}
        >>> analyser_notes([10, "abc", 25, -3, 14])
        {'moyenne': 12.0, 'admis': 2, 'recales': 0, 'meilleure': 14, 'mention': 'Assez bien'}
    """
    pass
