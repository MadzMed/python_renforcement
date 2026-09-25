# Exercice 1 : conditions et boucles

## Objectif

Vérifier que vous maîtrisez le **contrôle de flux** en Python :

- les conditions : `if` / `elif` / `else`
- les boucles : `for`
- la combinaison des deux

Vous manipulerez plusieurs types : `int`, `float`, `bool`, `str`, `list`, `dict` et `None`.

## Fichiers

| Fichier            | Rôle                                         |
|--------------------|----------------------------------------------|
| `exercise.py`      | **À compléter** : les 3 fonctions à écrire   |
| `test_exercise.py` | Les tests qui vérifient votre code (ne pas modifier) |
| `README.md`        | Ce document                                  |

## Consignes

1. Ouvrez `exercise.py`.
2. Dans chaque fonction, remplacez `pass` par votre code.
3. **Ne changez pas** le nom des fonctions ni leurs paramètres.
4. Aucun `import` n'est nécessaire.
5. Lancez les tests régulièrement pour vérifier votre avancement.

---

## Partie 1 : `categoriser_temperature(temperature)` (conditions)

Retourne une catégorie (`str`) selon la température.

| Température               | Résultat      |
|---------------------------|---------------|
| `< 0`                     | `"glacial"`   |
| de `0` à moins de `15`    | `"froid"`     |
| de `15` à moins de `25`   | `"doux"`      |
| `>= 25`                   | `"chaud"`     |
| pas un `int` ni un `float`| `"invalide"`  |

Attention : en Python, `True` et `False` sont aussi des `int`. Ils doivent donner `"invalide"`.

```python
categoriser_temperature(-5)    # 'glacial'
categoriser_temperature(15)    # 'doux'
categoriser_temperature(30.5)  # 'chaud'
categoriser_temperature("20")  # 'invalide'
categoriser_temperature(True)  # 'invalide'
```

---

## Partie 2 : `compter_voyelles(texte)` (boucles)

Parcourt un texte (`str`) et retourne un dictionnaire (`dict`) qui compte chaque voyelle.

- Le dictionnaire contient **toujours** les 6 clés : `"a"`, `"e"`, `"i"`, `"o"`, `"u"`, `"y"`.
- Les majuscules comptent comme des minuscules.
- Les lettres accentuées (`é`, `è`, `à`...) ne sont **pas** comptées.

```python
compter_voyelles("Bonjour")
# {'a': 0, 'e': 0, 'i': 0, 'o': 2, 'u': 1, 'y': 0}

compter_voyelles("")
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
```

---

## Partie 3 : `analyser_notes(notes)` (boucles + conditions)

Reçoit une liste (`list`) de notes et retourne un bilan (`dict`).

**Note valide** : un `int` ou un `float` (pas un `bool`) compris entre `0` et `20` inclus.
Toutes les autres valeurs sont **ignorées**.

| Clé           | Contenu                                         |
|---------------|-------------------------------------------------|
| `"moyenne"`   | moyenne des notes valides, arrondie à 2 décimales |
| `"admis"`     | nombre de notes `>= 10`                         |
| `"recales"`   | nombre de notes `< 10`                          |
| `"meilleure"` | la note la plus haute                           |
| `"mention"`   | calculée à partir de la moyenne (voir ci-dessous) |

| Moyenne  | Mention          |
|----------|------------------|
| `>= 16`  | `"Très bien"`    |
| `>= 14`  | `"Bien"`         |
| `>= 12`  | `"Assez bien"`   |
| `>= 10`  | `"Passable"`     |
| `< 10`   | `"Insuffisant"`  |

S'il n'y a **aucune note valide**, retournez :

```python
{"moyenne": 0.0, "admis": 0, "recales": 0, "meilleure": None, "mention": "Aucune note"}
```

**Contrainte** : n'utilisez pas `sum()`, `max()` ni `len()` sur les notes valides. Calculez le total, le compteur et la meilleure note vous-même dans la boucle.

```python
analyser_notes([12, 8, 15.5])
# {'moyenne': 11.83, 'admis': 2, 'recales': 1, 'meilleure': 15.5, 'mention': 'Passable'}

analyser_notes([10, "abc", 25, -3, 14])
# {'moyenne': 12.0, 'admis': 2, 'recales': 0, 'meilleure': 14, 'mention': 'Assez bien'}
```

---

## Lancer les tests

Depuis le dossier `1. exercise` :

```bash
pip install pytest
pytest test_exercise.py -v
```

Au départ, tous les tests échouent : c'est normal. L'exercice est terminé quand **tous les tests passent**.

Pour ne lancer que les tests d'une partie :

```bash
pytest test_exercise.py -v -k Temperature
pytest test_exercise.py -v -k Voyelles
pytest test_exercise.py -v -k Notes
```

## Indices

- `isinstance(x, (int, float))` vérifie le type d'une variable.
- `isinstance(True, int)` vaut `True`. Pensez à exclure les `bool` à part.
- `texte.lower()` met un texte en minuscules.
- `lettre in "aeiouy"` teste si un caractère est une voyelle.
- `round(valeur, 2)` arrondit à 2 décimales.
- Pour la meilleure note, gardez en mémoire la plus grande valeur vue jusqu'ici.

## Bonus

- Réécrivez `compter_voyelles` avec une boucle `while` au lieu d'un `for`.
- Ajoutez à `analyser_notes` une clé `"pire"` qui contient la note la plus basse.
