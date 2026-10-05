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
def categoriser_temperature(temperature: int | float):
    if type(temperature) != int and type(temperature) != float: # guard clause
        return "invalide"

    if temperature < 0:
        return "glacial"

    if temperature < 15:
        return "froid"

    if temperature < 25:
        return "doux"

    return "chaud"

# ---------------------------------------------------------------------------
# Partie 2 : les boucles (for)
# ---------------------------------------------------------------------------
def compter_voyelles(text: str):
    # initialiser mon dictionnaire
    counter = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}

    # si texte vide retourner dict avec des 0
    if text == "":
        return counter

    for char in text.lower():
        if char in counter:
            counter[char] += 1

    return counter

# ---------------------------------------------------------------------------
# Partie 3 : boucles + conditions
# ---------------------------------------------------------------------------
def analyser_notes(notes):
    total = 0
    count = 0 
    recales = 0
    admis = 0
    meilleur = None
    mention = "Aucune note"

    for note in  notes:
        if type(note) != int and type(note) != float or note < 0 or note > 20:
            continue

        if meilleur is None or meilleur < note:
            meilleur = note 

        total += note
        count += 1

        if note >= 10:
            admis += 1
        else:
            recales += 1

    if count != 0:
        moyenne = total / count
    else: 
        moyenne = 0.0

    if moyenne >= 16: 
        mention = "Très bien"
    elif moyenne >=14:
        mention = "Bien"
    elif moyenne >=12:
        mention = "Assez bien"
    elif moyenne >= 10:
        mention = "Passable"
    elif count == 0:
        mention = "Aucune note"
    else:
        mention = "Insuffisant"

    return {"moyenne": round(moyenne, 2), "admis": admis, "recales": recales,
            "meilleure": meilleur, "mention": mention}

        

    
