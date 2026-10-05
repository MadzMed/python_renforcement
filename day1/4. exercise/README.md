# Exercice 4 : programmation orientée objet avec un jeu de rôle

## Objectif

Construire le moteur d'un petit **jeu de rôle (RPG)** : des personnages de plusieurs classes (guerrier, mage, archer), des niveaux et de l'expérience, un inventaire, des objets et des combats.

Le jeu est **déterministe** : pas de hasard, les mêmes actions donnent toujours le même résultat. C'est ce qui permet de le tester.

## Les notions de POO à mettre en œuvre

| Notion                                  | Où ?                                                          |
|-----------------------------------------|---------------------------------------------------------------|
| Classe, `__init__`, attributs d'instance | toutes les classes                                           |
| Attributs de classe                     | `Personnage.nombre_personnages`, `PV_BASE`, `ATTAQUE_BASE`... |
| Encapsulation, `@property`, setter      | `pv` (stocké dans `_pv`), `est_vivant`                        |
| Héritage, `super()`                     | `Guerrier`, `Mage`, `Archer` héritent de `Personnage`         |
| Classe et méthode abstraites            | `Personnage` (hérite de `ABC`), `attaquer` (`@abstractmethod`) |
| Polymorphisme                           | chaque classe a sa propre méthode `attaquer`                  |
| Méthode statique                        | `Personnage.xp_pour_niveau` (`@staticmethod`)                 |
| Méthode de classe                       | `Personnage.depuis_dict` (`@classmethod`)                     |
| Méthodes spéciales                      | `__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__`, `__contains__` |
| Composition                             | un `Personnage` **a un** `Inventaire` qui **contient des** `Objet` ; un `Combat` **a deux** `Personnage` |
| Exception personnalisée                 | `ActionImpossible` (hérite de `Exception`)                    |

## Fichiers

| Fichier            | Rôle                                                  |
|--------------------|-------------------------------------------------------|
| `rpg.py`           | **À compléter** : toutes les classes du jeu           |
| `test_exercise.py` | Les tests qui vérifient votre code (ne pas modifier)  |
| `README.md`        | Ce document                                           |

## Consignes

1. Dans `rpg.py`, toutes les classes et méthodes existent déjà, mais elles sont **vides**.
2. À vous d'ajouter les **classes parentes**, les **décorateurs**, les **attributs** et le **code** des méthodes. Les commentaires `TODO` indiquent ce qui manque.
3. **Ne changez pas** le nom des classes, des méthodes ni des paramètres.
4. Avancez **partie par partie** (1 → 4) et lancez les tests de chaque partie au fur et à mesure.

---

## Schéma des classes

```
                    ┌───────────────────────────────┐
                    │ Personnage (ABC)   abstraite  │
                    ├───────────────────────────────┤
                    │ nombre_personnages   (classe) │
                    │ PV_BASE, ATTAQUE_BASE,        │
                    │ DEFENSE_BASE         (classe) │
                    │ nom, niveau, experience       │
                    │ pv_max, _pv, attaque, defense │
                    │ inventaire ───────────────────┼──► Inventaire ──► Objet (0..capacite)
                    ├───────────────────────────────┤
                    │ pv            (property)      │
                    │ est_vivant    (property)      │
                    │ subir_degats(), soigner()     │
                    │ gagner_experience()           │
                    │ monter_niveau()               │
                    │ utiliser_objet()              │
                    │ verifier_attaque()            │
                    │ attaquer()    (abstraite)     │
                    │ xp_pour_niveau()  (statique)  │
                    │ depuis_dict()     (de classe) │
                    │ __str__ __repr__ __eq__ __lt__│
                    └───────────────▲───────────────┘
                                    │ hérite de
             ┌──────────────────────┼──────────────────────┐
     ┌───────┴───────┐      ┌───────┴───────┐      ┌───────┴───────┐
     │   Guerrier    │      │     Mage      │      │    Archer     │
     │ attaquer()    │      │ mana, mana_max│      │ nombre_tirs   │
     │  (rage)       │      │ attaquer()    │      │ attaquer()    │
     │               │      │ monter_niveau()│     │  (critique)   │
     └───────────────┘      └───────────────┘      └───────────────┘

  Combat : p1, p2, journal, nombre_tours, est_termine, vainqueur, tour(), lancer()
  ActionImpossible(Exception)
```

---

## Partie 1 : exception, objets et inventaire

**`ActionImpossible`** : une exception à lever quand une action est interdite. Il suffit de la faire hériter de `Exception`.

**`Objet(nom, type, valeur)`** : `type` vaut `"soin"` ou `"arme"`, sinon `ValueError`.

```python
repr(Objet("Potion", "soin", 30))   # "Objet('Potion', 'soin', 30)"
```

**`Inventaire(capacite=5)`** :

| Méthode             | Rôle                                                            |
|---------------------|-----------------------------------------------------------------|
| `ajouter(objet)`    | ajoute l'objet ; `ActionImpossible` si l'inventaire est plein   |
| `retirer(nom)`      | retire le premier objet de ce nom et le **retourne** ; `ActionImpossible` s'il est absent |
| `len(sac)`          | nombre d'objets (`__len__`)                                     |
| `"Potion" in sac`   | `True` si un objet porte ce nom (`__contains__`)                |

## Partie 2 : la classe `Personnage`

`Personnage` est **abstraite** : `Personnage("Bob")` doit lever une `TypeError`. Seules ses classes filles sont jouables.

### Attributs

- De **classe** : `nombre_personnages = 0`, `PV_BASE = 100`, `ATTAQUE_BASE = 10`, `DEFENSE_BASE = 0`.
- D'**instance** : `nom`, `niveau = 1`, `experience = 0`, `pv_max`, `_pv`, `attaque`, `defense` (tirés des constantes de la classe, avec `self.PV_BASE`...) et un **nouvel** `Inventaire`.
- Chaque création de personnage incrémente `Personnage.nombre_personnages`.

### Encapsulation

- `pv` est une **propriété** : la valeur est stockée dans `_pv`, et le **setter** la borne entre `0` et `pv_max`.
- `est_vivant` est une propriété **en lecture seule** : `True` si `pv > 0`.

```python
g = Guerrier("Aragorn")
g.pv = -50      # g.pv vaut 0
g.pv = 9999     # g.pv vaut 120
```

### Règles du jeu

| Méthode                    | Règle                                                                  |
|----------------------------|------------------------------------------------------------------------|
| `subir_degats(montant)`    | dégâts réels = `max(1, montant - defense)`, retirés des pv ; retourne les dégâts réels |
| `soigner(montant)`         | pv + montant, sans dépasser `pv_max` ; retourne les pv gagnés ; `ActionImpossible` si mort |
| `xp_pour_niveau(niveau)`   | **statique** : `niveau * 100`                                          |
| `gagner_experience(xp)`    | ajoute l'xp ; tant que `experience >= xp_pour_niveau(niveau)`, retire ce montant et monte de niveau ; retourne le nombre de niveaux gagnés |
| `monter_niveau()`          | niveau +1, pv_max +10, attaque +2, defense +1, pv remis au max         |
| `utiliser_objet(nom)`      | retire l'objet de l'inventaire : `"soin"` → soigne, `"arme"` → attaque + valeur ; `ActionImpossible` si mort ou objet absent |
| `verifier_attaque(cible)`  | `ActionImpossible` si la cible est soi-même, ou si l'un des deux est mort |
| `attaquer(cible)`          | **abstraite** : chaque classe fille la redéfinit                       |
| `depuis_dict(donnees)`     | **de classe** : crée un personnage de la classe `cls` au niveau demandé |

```python
g = Guerrier("Aragorn")
g.subir_degats(20)           # 15  (20 - 5 de défense)
g.gagner_experience(350)     # 2   -> niveau 3, experience 50

m = Mage.depuis_dict({"nom": "Merlin", "niveau": 3})
type(m).__name__, m.niveau   # ('Mage', 3)
```

### Méthodes spéciales

```python
g = Guerrier("Aragorn")
str(g)     # 'Aragorn (Guerrier) - niveau 1 - PV 120/120'
repr(g)    # "Guerrier('Aragorn', niveau=1)"

Guerrier("Bob") == Guerrier("Bob")   # True  (même classe, nom et niveau)
Guerrier("Bob") == Archer("Bob")     # False (classes différentes)
sorted(personnages)                  # trié par niveau grâce à __lt__
```

## Partie 3 : les classes de personnages

| Classe     | PV  | Attaque | Défense | Particularité                                             |
|------------|-----|---------|---------|-----------------------------------------------------------|
| `Guerrier` | 120 | 15      | 5       | **Rage** : si pv < 30 % de pv_max, dégâts envoyés ×2      |
| `Mage`     | 80  | 8       | 2       | **Mana** 50 : si mana ≥ 10, dépense 10 et envoie `attaque × 3` ; sinon `attaque` |
| `Archer`   | 100 | 12      | 3       | **Critique** : tous les 3 tirs (3e, 6e...), dégâts ×2     |

- Chaque `attaquer(cible)` commence par `self.verifier_attaque(cible)`, envoie ses dégâts avec `cible.subir_degats(...)` et **retourne les dégâts réels**.
- `Mage.__init__` et `Archer.__init__` appellent d'abord `super().__init__(nom)`, puis ajoutent leurs propres attributs.
- `Mage.monter_niveau()` appelle `super().monter_niveau()`, puis ajoute 10 au `mana_max` et remplit le mana.

```python
cible = Guerrier("Cible")          # défense 5
Guerrier("G").attaquer(cible)      # 10  (15 - 5)
Mage("M").attaquer(cible)          # 19  (8 × 3 - 5)
Archer("A").attaquer(cible)        # 7   (12 - 5)
```

C'est le **polymorphisme** : le même appel `perso.attaquer(cible)` donne un résultat différent selon la classe du personnage.

## Partie 4 : le combat

**`Combat(p1, p2)`** : `ActionImpossible` si `p1` et `p2` sont le même objet, ou si l'un des deux est mort.

| Membre              | Rôle                                                                     |
|---------------------|--------------------------------------------------------------------------|
| `journal`           | liste de phrases, vide au départ                                         |
| `nombre_tours`      | 0 au départ                                                              |
| `est_termine`       | **propriété** : `True` si l'un des deux est mort                        |
| `vainqueur`         | **propriété** : le survivant si le combat est terminé, sinon `None`     |
| `tour()`            | p1 attaque p2, puis p2 riposte **s'il est encore vivant** ; une ligne par attaque dans le journal ; `ActionImpossible` si le combat est déjà terminé |
| `lancer(max_tours=100)` | joue les tours jusqu'à la fin ; le vainqueur gagne `50 × niveau du perdant` XP ; ajoute `"<nom> remporte le combat"` au journal ; retourne le vainqueur (ou `None` si `max_tours` est atteint) |

```python
g, m = Guerrier("Aragorn"), Mage("Merlin")
combat = Combat(g, m)
combat.tour()
combat.journal
# ['Aragorn inflige 13 dégâts à Merlin', 'Merlin inflige 19 dégâts à Aragorn']

combat.lancer()     # Aragorn  (il gagne 50 XP)
```

---

## Lancer les tests

Depuis le dossier `4. exercise` :

```bash
pip install pytest
pytest test_exercise.py -v
```

Pour ne tester qu'une partie :

```bash
pytest test_exercise.py -v -k Partie1
pytest test_exercise.py -v -k Partie2
pytest test_exercise.py -v -k Partie3
pytest test_exercise.py -v -k Partie4
```

La plupart des tests créent des `Guerrier`, `Mage` ou `Archer`. Commencez donc par la partie 1, puis la partie 2, puis faites **au moins** hériter les trois classes de `Personnage` avec leurs constantes avant de revenir aux tests de la partie 2.

L'exercice est terminé quand **tous les tests passent**.

## Indices

- Une propriété avec setter :

  ```python
  @property
  def pv(self):
      return self._pv

  @pv.setter
  def pv(self, valeur):
      ...
  ```

- Dans `__init__`, écrivez `self.pv_max = self.PV_BASE` : Python cherche `PV_BASE` d'abord dans la classe réelle de l'objet (`Guerrier`), puis dans `Personnage`.
- Pour le compteur, écrivez `Personnage.nombre_personnages += 1` et non `self.nombre_personnages += 1` (qui créerait un attribut sur l'instance).
- `type(self).__name__` donne le nom de la classe (`"Guerrier"`).
- Dans une méthode de classe, `cls(nom)` crée un objet de la classe sur laquelle la méthode a été appelée : `Mage.depuis_dict(...)` crée un `Mage`.
- Dans `soigner`, retenez les pv **avant** de soigner pour calculer le gain.

## Bonus

- Ajouter une classe `Soigneur` qui, au lieu de frapper fort, se soigne de 10 pv à chaque attaque.
- Ajouter une hiérarchie `Monstre` (`Gobelin`, `Dragon`) qui peut combattre les personnages.
- Ajouter des coups critiques **aléatoires** en passant un objet `random.Random(graine)` au constructeur, pour que les tests restent reproductibles.
- Ajouter une classe `Equipe` qui contient plusieurs personnages et un combat équipe contre équipe.
