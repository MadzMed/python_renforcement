# Exercice 3 : vérificateur de sudoku

## Objectif

Écrire un programme qui dit si une grille de sudoku **déjà remplie** est correcte ou non.

Vous allez pratiquer :

- les **boucles imbriquées** (une boucle dans une boucle, dans une boucle...)
- les listes de listes et les index `grille[ligne][colonne]`
- l'écriture d'un **algorithme** : découper un gros problème en petites fonctions

## Rappel : les règles du sudoku

Une grille de sudoku fait 9 × 9 cases. Elle est correcte si :

1. chaque **ligne** contient les nombres de 1 à 9, une seule fois chacun ;
2. chaque **colonne** contient les nombres de 1 à 9, une seule fois chacun ;
3. chacun des 9 **carrés 3 × 3** contient les nombres de 1 à 9, une seule fois chacun.

## Fichiers

| Fichier            | Rôle                                                  |
|--------------------|-------------------------------------------------------|
| `grilles.py`       | Des grilles d'exemple, justes et fausses (**ne pas modifier**) |
| `exercise.py`      | **À compléter** : les 5 fonctions à écrire            |
| `test_exercise.py` | Les tests qui vérifient votre code (ne pas modifier)  |
| `README.md`        | Ce document                                           |

## Consignes

1. Complétez les fonctions de `exercise.py` **dans l'ordre** : chaque fonction utilise les précédentes.
2. **Ne changez pas** le nom des fonctions ni leurs paramètres.
3. **Interdit** : `set()` et `sorted()`. Le but est d'écrire l'algorithme vous-même avec des boucles.
4. **Ne modifiez pas** la grille reçue.

---

## La grille en Python

Une grille est une **liste de 9 lignes**, chaque ligne est une **liste de 9 entiers** :

```python
grille = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],   # grille[0]  -> ligne 0
    [6, 7, 2, 1, 9, 5, 3, 4, 8],   # grille[1]  -> ligne 1
    ...
]

grille[0]      # la ligne 0 : [5, 3, 4, 6, 7, 8, 9, 1, 2]
grille[1][4]   # ligne 1, colonne 4 : 9
```

Les 9 carrés sont numérotés ainsi :

```
         colonnes 0-2   colonnes 3-5   colonnes 6-8
        +--------------+--------------+--------------+
lignes  |              |              |              |
 0-2    |   carré 0    |   carré 1    |   carré 2    |
        +--------------+--------------+--------------+
lignes  |              |              |              |
 3-5    |   carré 3    |   carré 4    |   carré 5    |
        +--------------+--------------+--------------+
lignes  |              |              |              |
 6-8    |   carré 6    |   carré 7    |   carré 8    |
        +--------------+--------------+--------------+
```

Un carré commence toujours à une ligne **0, 3 ou 6** et à une colonne **0, 3 ou 6**.
Pour le carré numéro `c`, la case en haut à gauche est `(3 * (c // 3), 3 * (c % 3))`.

---

## Étape 1 : `groupe_valide(groupe)`

Vérifie **une liste de 9 cases** (une ligne, une colonne ou un carré).
Retourne `True` si elle contient exactement les nombres 1 à 9, chacun une seule fois.

Elle retourne `False` si la liste n'a pas 9 éléments, si un élément n'est pas un `int` (attention : `True` est un `int` en Python !), s'il n'est pas entre 1 et 9, ou s'il y a un doublon.

```python
groupe_valide([5, 3, 4, 6, 7, 8, 9, 1, 2])   # True
groupe_valide([5, 3, 4, 6, 7, 8, 9, 1, 5])   # False (deux 5)
groupe_valide([0, 3, 4, 6, 7, 8, 9, 1, 2])   # False (0 interdit)
groupe_valide([1, 2, 3])                     # False (pas 9 éléments)
```

Idée d'algorithme : une liste `deja_vu = [False] * 10`. Pour chaque nombre `n`, si `deja_vu[n]` vaut déjà `True`, c'est un doublon. Sinon, on le passe à `True`.

## Étape 2 : `lignes_valides(grille)`

Retourne `True` si les 9 lignes sont valides. Une ligne, c'est simplement `grille[i]`.

## Étape 3 : `colonnes_valides(grille)`

Retourne `True` si les 9 colonnes sont valides.
Une colonne n'existe pas toute faite : il faut la **construire** avec une boucle dans une boucle.

```
colonne 0 = [grille[0][0], grille[1][0], grille[2][0], ..., grille[8][0]]
```

## Étape 4 : `carres_valides(grille)`

Retourne `True` si les 9 carrés 3 × 3 sont valides.
Pour chaque carré, rassemblez ses 9 cases dans une liste. Il faut des boucles imbriquées : une pour choisir le carré, deux pour parcourir ses cases.

```
carré 0 = [grille[0][0], grille[0][1], grille[0][2],
           grille[1][0], grille[1][1], grille[1][2],
           grille[2][0], grille[2][1], grille[2][2]]
```

## Étape 5 : `sudoku_valide(grille)`

La fonction finale :

1. vérifiez le **format** : `grille` est une `list` de 9 lignes, et chaque ligne est une `list` de 9 éléments. Sinon, retournez `False` sans planter ;
2. vérifiez les lignes, les colonnes et les carrés.

```python
from grilles import GRILLE_VALIDE, GRILLE_CARRE_FAUSSE

sudoku_valide(GRILLE_VALIDE)         # True
sudoku_valide(GRILLE_CARRE_FAUSSE)   # False
sudoku_valide([[1, 2, 3]])           # False
```

## Les grilles d'exemple (`grilles.py`)

| Grille                  | Lignes | Colonnes | Carrés |
|-------------------------|:------:|:--------:|:------:|
| `GRILLE_VALIDE`         | ✅     | ✅       | ✅     |
| `GRILLE_LIGNE_FAUSSE`   | ❌     | ✅       | ✅     |
| `GRILLE_COLONNE_FAUSSE` | ✅     | ❌       | ✅     |
| `GRILLE_CARRE_FAUSSE`   | ✅     | ✅       | ❌     |

Chaque grille fausse ne casse **qu'une seule** règle : c'est ce qui permet de vérifier que chacune de vos fonctions teste bien la bonne chose.

---

## Lancer les tests

Depuis le dossier `3. exercise` :

```bash
pip install pytest
pytest test_exercise.py -v
```

Pour ne tester qu'une étape :

```bash
pytest test_exercise.py -v -k Groupe
pytest test_exercise.py -v -k Lignes
pytest test_exercise.py -v -k Colonnes
pytest test_exercise.py -v -k Carres
pytest test_exercise.py -v -k Sudoku
```

L'exercice est terminé quand **tous les tests passent**.

## Indices

- `range(0, 9, 3)` donne `0, 3, 6` : pratique pour les débuts de carrés.
- Pour construire une colonne ou un carré, partez d'une liste vide `[]` et utilisez `.append()`.
- Dès qu'un groupe est faux, vous pouvez faire `return False` immédiatement. `return True` ne vient qu'**après** la boucle.
- Pour exclure les `bool` : `isinstance(x, bool)` est vrai pour `True` et `False`.

## Bonus

- `trouver_erreurs(grille)` : retourner la liste des problèmes trouvés, par exemple `["ligne 0", "colonne 3", "carré 4"]`.
- Rendre le vérificateur **générique** : accepter des grilles 4 × 4 (carrés 2 × 2) ou 16 × 16 (carrés 4 × 4).
- `carres_valides` en une seule boucle `for c in range(9)` en utilisant la formule `(3 * (c // 3), 3 * (c % 3))`.
