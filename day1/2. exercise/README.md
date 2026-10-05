# Exercice 2 : accéder aux données d'une structure complexe

## Objectif

Savoir **lire des données dans une structure imbriquée** : un dictionnaire qui contient des listes, qui contiennent des dictionnaires, qui contiennent des tuples, des sets...

Vous allez pratiquer :

- l'accès par clé `d["cle"]` et par index `liste[0]`, `liste[-1]`
- l'enchaînement des accès `d["a"]["b"][0]["c"]`
- le parcours d'une structure avec des boucles
- l'accès **sécurisé** : ne pas planter quand une donnée est absente

## Fichiers

| Fichier            | Rôle                                                   |
|--------------------|--------------------------------------------------------|
| `donnees.py`       | La structure `ECOLE` à explorer (**ne pas modifier**)  |
| `exercise.py`      | **À compléter** : les 9 fonctions à écrire             |
| `test_exercise.py` | Les tests qui vérifient votre code (ne pas modifier)   |
| `README.md`        | Ce document                                            |

## Consignes

1. Lisez d'abord `donnees.py` pour comprendre la structure.
2. Dans `exercise.py`, remplacez chaque `pass` par votre code.
3. **Ne changez pas** le nom des fonctions ni leurs paramètres.
4. Utilisez **toujours** le paramètre `donnees`, jamais `ECOLE` directement. Les tests utilisent aussi d'autres structures : une réponse écrite « en dur » (ex. `return "Lyon"`) échouera.
5. **Ne modifiez pas** la structure reçue : vos fonctions ne font que lire.

---

## Carte de la structure

```
ECOLE                                  dict
├── "nom"                              str
├── "adresse"                          dict
│   ├── "ville"                        str
│   ├── "code_postal"                  str
│   └── "coordonnees"                  tuple (latitude, longitude)
└── "classes"                          list
    └── [i]                            dict  (une classe)
        ├── "nom"                      str
        ├── "professeur"               dict
        │   ├── "nom"                  str
        │   └── "contact"              dict
        │       ├── "email"            str
        │       └── "telephones"       list de str
        ├── "horaires"                 dict  (jour -> list)
        │   └── "lundi"                list de tuple ("début", "fin")
        └── "eleves"                   list
            └── [j]                    dict  (un élève)
                ├── "id"               int
                ├── "prenom"           str
                ├── "age"              int
                ├── "actif"            bool
                ├── "notes"            dict  (matière -> list de notes)
                ├── "options"          set de str
                └── "tuteur"           None ou dict {"nom", "telephone"}
```

Attention aux cas particuliers : un élève peut ne pas avoir une matière, avoir une liste de notes vide, ou ne pas avoir de notes du tout (`{}`).

---

## Niveau 1 : accès direct (clés et index)

| Fonction                                | Retourne                                           | Exemple sur `ECOLE`             |
|-----------------------------------------|----------------------------------------------------|---------------------------------|
| `ville_ecole(donnees)`                  | la ville de l'école                                | `'Lyon'`                        |
| `latitude_ecole(donnees)`               | le 1er élément du tuple `coordonnees`              | `45.76`                         |
| `email_professeur(donnees, index_classe)` | l'email du prof de la classe n° `index_classe`   | `(ECOLE, 0)` → `'martin@academie-python.fr'` |
| `dernier_telephone(donnees, index_classe)` | le **dernier** téléphone de ce prof             | `(ECOLE, 0)` → `'04 72 00 00 01'` |

## Niveau 2 : parcourir la structure (boucles)

**`prenoms_eleves(donnees)`** retourne la liste des prénoms de tous les élèves, classe après classe.

```python
prenoms_eleves(ECOLE)
# ['Alice', 'Bilal', 'Chloé', 'David', 'Emma', 'Farid', 'Gaëlle', 'Hugo']
```

**`trouver_eleve(donnees, id_eleve)`** retourne le dictionnaire de l'élève qui a cet `id`, ou `None`.

```python
trouver_eleve(ECOLE, 5)["prenom"]   # 'Emma'
trouver_eleve(ECOLE, 99)            # None
```

**`moyenne_eleve(donnees, prenom, matiere)`** retourne la moyenne (arrondie à 2 décimales) de l'élève dans la matière. Elle retourne `None` si l'élève n'existe pas, s'il n'a pas la matière, ou si sa liste de notes est vide.

```python
moyenne_eleve(ECOLE, "Alice", "python")   # 13.75
moyenne_eleve(ECOLE, "Bilal", "sql")      # None  (pas de clé "sql")
moyenne_eleve(ECOLE, "Chloé", "python")   # None  (liste vide)
```

## Niveau 3 : accès sécurisé et regroupement

**`eleves_par_option(donnees)`** regroupe les prénoms par option, chaque liste étant triée par ordre alphabétique.

```python
eleves_par_option(ECOLE)
# {'sport':   ['Alice', 'David', 'Farid'],
#  'cantine': ['Alice', 'Bilal', 'Farid', 'Gaëlle'],
#  'théâtre': ['David', 'Emma', 'Farid']}
```

**`acces_chemin(donnees, chemin)`** suit une liste de clés et d'index et retourne la valeur au bout du chemin :

- élément courant `dict` → l'étape est une clé
- élément courant `list` ou `tuple` → l'étape est un index `int` (négatif autorisé)
- étape impossible (clé absente, index hors limites, mauvais type...) → `None`
- chemin vide → `donnees` lui-même

```python
acces_chemin(ECOLE, ["classes", 0, "professeur", "nom"])     # 'Martin'
acces_chemin(ECOLE, ["classes", 0, "horaires", "lundi", 0, 1])  # '12:00'
acces_chemin(ECOLE, ["adresse", "coordonnees", -1])          # 4.83
acces_chemin(ECOLE, ["classes", 10, "nom"])                  # None
acces_chemin(ECOLE, ["classes", 0, "eleves", 0, "tuteur", "nom"])  # None (tuteur vaut None)
```

Pas besoin de `try/except` : `in`, `len()` et `isinstance()` suffisent.

---

## Lancer les tests

Depuis le dossier `2. exercise` :

```bash
pip install pytest
pytest test_exercise.py -v
```

Pour ne lancer qu'un niveau :

```bash
pytest test_exercise.py -v -k Niveau1
pytest test_exercise.py -v -k Niveau2
pytest test_exercise.py -v -k Niveau3
```

L'exercice est terminé quand **tous les tests passent**.

## Indices

- Construisez l'accès **étape par étape** : testez d'abord `donnees["classes"]`, puis `donnees["classes"][0]`, puis `donnees["classes"][0]["professeur"]`...
- `print(type(x))` vous dit à quel type vous avez affaire.
- `liste[-1]` donne le dernier élément.
- `d.get("cle")` retourne `None` au lieu de planter si la clé est absente. `d.get("cle", [])` retourne `[]` à la place.
- `"cle" in d` teste si une clé existe.
- Pour un index `i` dans une liste `l`, il est valide si `-len(l) <= i < len(l)`.
- `sorted(liste)` retourne une nouvelle liste triée.

## Bonus

- `classe_la_plus_nombreuse(donnees)` : le nom de la classe qui a le plus d'élèves.
- `eleves_sans_tuteur(donnees)` : les prénoms des élèves dont le tuteur vaut `None`.
- `creneaux_du_jour(donnees, jour)` : tous les créneaux `(début, fin)` de ce jour, toutes classes confondues.
