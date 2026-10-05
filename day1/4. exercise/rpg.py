"""
Exercice 4 : programmation orientée objet avec un jeu de rôle
=============================================================

Complétez ce fichier en suivant les consignes du README et des docstrings.

Toutes les classes et méthodes existent déjà, mais elles sont VIDES.
C'est à vous d'ajouter :
    - les classes parentes (héritage),
    - les décorateurs (@property, @staticmethod, @classmethod, @abstractmethod),
    - les attributs (de classe et d'instance),
    - le code des méthodes (remplacez `pass`).

Ne changez PAS le nom des classes, des méthodes ni des paramètres.

Lancez les tests avec :  pytest test_exercise.py -v
"""

from abc import ABC, abstractmethod


# ===========================================================================
# Partie 1 : exception, objets et inventaire
# ===========================================================================
class ActionImpossible(Exception):
    """
    Exception levée quand une action est interdite par les règles du jeu
    (attaquer un mort, inventaire plein, objet absent...).

    TODO : cette classe doit hériter de Exception. Son corps peut rester `pass`.
    """

    pass


class Objet:
    """
    Un objet que l'on peut ranger dans un inventaire.

    TODO attributs d'instance : nom (str), type (str), valeur (int)
    """

    def __init__(self, nom, type, valeur):
        """
        `type` doit valoir "soin" ou "arme".
        Sinon, lever une ValueError.
        """
        pass

    def __repr__(self):
        """
        >>> repr(Objet("Potion", "soin", 30))
        "Objet('Potion', 'soin', 30)"
        """
        pass


class Inventaire:
    """
    Un sac qui contient des Objet.

    TODO attributs d'instance :
        capacite (int) : nombre maximum d'objets
        objets (list)  : liste des objets, vide au départ
    """

    def __init__(self, capacite=5):
        self.capacite = capacite
        self.objets = []

    def ajouter(self, objet):
        """Ajoute l'objet. Lève ActionImpossible si l'inventaire est plein."""
        if len(self.objets) >= self.capacite:
            raise ActionImpossible("Inventaire plein")

        self.objets.append(objet)

    def retirer(self, nom):
        """
        Retire le PREMIER objet qui porte ce nom et le RETOURNE.
        Lève ActionImpossible si aucun objet ne porte ce nom.
        """
        for i, objet in enumerate(self.objets):
            if objet.nom == nom:
                return self.objets.pop(i)

        raise ActionImpossible(f"Aucun objet nommé '{nom}'")

    def __len__(self):  # len(Inventaire(5))
        """len(inventaire) retourne le nombre d'objets."""
        return len(self.objets)

    def __contains__(self, nom):  # "Potion" in Inventaire(5)
        """`"Potion" in inventaire` retourne True si un objet porte ce nom."""
        return any(objet.nom == nom for objet in self.objets)


# ===========================================================================
# Partie 2 : la classe de base Personnage
# ===========================================================================
class Personnage:
    """
    Classe de base de tous les personnages.

    TODO : cette classe doit être ABSTRAITE (hériter de ABC). On ne doit pas
    pouvoir écrire Personnage("Bob") : seules ses classes filles sont jouables.

    TODO attributs de CLASSE :
        nombre_personnages = 0   (compte tous les personnages créés)
        PV_BASE = 100
        ATTAQUE_BASE = 10
        DEFENSE_BASE = 0
    """

    nombre_personnages = 0
    PV_BASE = 100
    ATTAQUE_BASE = 10
    DEFENSE_BASE = 0

    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.experience = 0
        self.pv_max = self.PV_BASE
        self._pv = self.pv_max
        self.attaque = self.ATTAQUE_BASE
        self.defense = self.DEFENSE_BASE
        self.inventaire = Inventaire()

    # TODO : propriété `pv` (getter) qui retourne self._pv.
    def pv(self):
        return self._pv

    # TODO : setter de `pv` : la valeur est bornée entre 0 et pv_max.
    #        perso.pv = -50   ->  perso.pv vaut 0
    #        perso.pv = 9999  ->  perso.pv vaut pv_max
    def set_pv(self, valeur):
        if valeur < 0:
            self._pv = 0
        elif valeur > self.pv_max:
            self._pv = self.pv_max
        else:
            self._pv = valeur

    # TODO : propriété `est_vivant` (lecture seule, sans setter) :
    #        True si pv > 0.
    def est_vivant(self):
        return self._pv > 0

    def subir_degats(self, montant):
        """
        Les dégâts réels valent  max(1, montant - defense).
        Ils sont retirés des pv (qui ne descendent jamais sous 0).
        Retourne les dégâts réels.

        >>> g = Guerrier("Aragorn")   # defense 5
        >>> g.subir_degats(20)
        15
        >>> g.pv
        105
        """
        pass

    def soigner(self, montant):
        """
        Ajoute `montant` aux pv, sans dépasser pv_max.
        Retourne le nombre de pv réellement gagnés.
        Lève ActionImpossible si le personnage est mort.
        """
        pass

    # TODO : méthode STATIQUE
    def xp_pour_niveau(niveau):
        """
        Retourne l'expérience nécessaire pour passer du niveau `niveau`
        au suivant : niveau * 100.

        >>> Personnage.xp_pour_niveau(3)
        300
        """
        pass

    def gagner_experience(self, xp):
        """
        Ajoute `xp` à l'expérience. Tant que l'expérience atteint
        xp_pour_niveau(niveau) : on retire ce montant et on monte d'un niveau.
        Retourne le nombre de niveaux gagnés.

        >>> g = Guerrier("Aragorn")
        >>> g.gagner_experience(350)   # 100 pour le niv 2, 200 pour le niv 3
        2
        >>> g.niveau, g.experience
        (3, 50)
        """
        pass

    def monter_niveau(self):
        """
        niveau +1, pv_max +10, attaque +2, defense +1,
        et les pv remontent au maximum.
        """
        pass

    def utiliser_objet(self, nom):
        """
        Retire l'objet `nom` de l'inventaire et l'utilise :
            - "soin" : soigne de `valeur` pv
            - "arme" : ajoute `valeur` à l'attaque
        Lève ActionImpossible si le personnage est mort (avant de retirer
        l'objet) ou si l'objet n'est pas dans l'inventaire.
        """
        pass

    def verifier_attaque(self, cible):
        """
        Lève ActionImpossible si :
            - la cible est le personnage lui-même,
            - l'attaquant est mort,
            - la cible est morte.
        À appeler au début de chaque méthode attaquer().
        """
        pass

    # TODO : méthode ABSTRAITE
    def attaquer(self, cible):
        """
        Attaque la cible et retourne les dégâts réels infligés.
        Chaque classe fille a sa propre façon d'attaquer (polymorphisme).
        """
        pass

    # TODO : méthode DE CLASSE
    def depuis_dict(cls, donnees):
        """
        Constructeur alternatif. Crée un personnage de la classe `cls`
        à partir d'un dict, puis le fait monter jusqu'au niveau demandé.
        "niveau" est optionnel (1 par défaut).

        >>> m = Mage.depuis_dict({"nom": "Merlin", "niveau": 3})
        >>> type(m).__name__, m.niveau
        ('Mage', 3)
        """
        pass

    def __str__(self):
        """
        >>> str(Guerrier("Aragorn"))
        'Aragorn (Guerrier) - niveau 1 - PV 120/120'
        """
        return f"Hey, salut, je suis {self.nom} ({type(self).__name__}) - niveau {self.niveau} - PV {self.pv}/{self.pv_max}"

    def __repr__(self):
        """
        >>> repr(Guerrier("Aragorn"))
        "Guerrier('Aragorn', niveau=1)"
        """
        return f"<{type(self).__name__}('{self.nom}', niveau={self.niveau})>"

    def __eq__(self, autre):
        """
        Deux personnages sont égaux s'ils sont de la MÊME classe et ont le
        même nom et le même niveau.
        Si `autre` n'est pas un Personnage, retourner NotImplemented.
        """
        pass

    def __lt__(self, autre):
        """
        p1 < p2 si p1 a un niveau plus petit.
        Cela permet d'écrire sorted(liste_de_personnages).
        """
        if not isinstance(autre, Personnage):
            return NotImplemented

        return self.niveau < autre.niveau


# ===========================================================================
# Partie 3 : les classes de personnages (héritage et polymorphisme)
# ===========================================================================
class Guerrier:
    """
    TODO : hérite de Personnage.
    TODO attributs de classe : PV_BASE = 120, ATTAQUE_BASE = 15, DEFENSE_BASE = 5
    """

    def attaquer(self, cible):
        """
        Inflige `attaque` à la cible.
        RAGE : si les pv du guerrier sont strictement inférieurs à 30 % de
        son pv_max, les dégâts envoyés sont doublés.
        Retourne les dégâts réels.
        """
        pass


class Mage:
    """
    TODO : hérite de Personnage.
    TODO attributs de classe : PV_BASE = 80, ATTAQUE_BASE = 8, DEFENSE_BASE = 2,
                               MANA_BASE = 50, COUT_SORT = 10
    """

    def __init__(self, nom):
        """
        Appelle le __init__ du parent avec super(), puis ajoute :
            mana_max = MANA_BASE
            mana     = mana_max
        """
        pass

    def attaquer(self, cible):
        """
        Si mana >= COUT_SORT : dépense COUT_SORT de mana et envoie
        attaque * 3 dégâts (boule de feu).
        Sinon : envoie `attaque` dégâts.
        Retourne les dégâts réels.
        """
        pass

    def monter_niveau(self):
        """
        Fait tout ce que fait le parent (super()), puis :
        mana_max +10 et le mana remonte au maximum.
        """
        pass


class Archer:
    """
    TODO : hérite de Personnage.
    TODO attributs de classe : PV_BASE = 100, ATTAQUE_BASE = 12, DEFENSE_BASE = 3
    """

    def __init__(self, nom):
        """
        Appelle le __init__ du parent, puis ajoute :
            nombre_tirs = 0
        """
        pass

    def attaquer(self, cible):
        """
        Chaque attaque augmente nombre_tirs de 1.
        Tous les 3 tirs (3e, 6e, 9e...), le tir est CRITIQUE : dégâts doublés.
        Retourne les dégâts réels.
        """
        pass


# ===========================================================================
# Partie 4 : le combat (composition)
# ===========================================================================
class Combat:
    """
    Un combat entre deux personnages.

    TODO attributs d'instance : p1, p2, journal (list de str, vide),
                                nombre_tours (0)
    """

    def __init__(self, p1, p2):
        """
        Lève ActionImpossible si p1 et p2 sont le même objet,
        ou si l'un des deux est mort.
        """
        pass

    # TODO : propriété `est_termine` : True si l'un des deux est mort.
    #
    # TODO : propriété `vainqueur` : le personnage encore vivant si le combat
    #        est terminé, sinon None.

    def tour(self):
        """
        Joue un tour :
            1. p1 attaque p2,
            2. puis, si p2 est encore vivant, p2 attaque p1.
        Chaque attaque ajoute une ligne au journal, par exemple :
            "Aragorn inflige 13 dégâts à Merlin"
        Puis nombre_tours augmente de 1.
        Lève ActionImpossible si le combat est déjà terminé.
        """
        pass

    def lancer(self, max_tours=100):
        """
        Joue des tours jusqu'à ce que le combat soit terminé, ou que
        max_tours tours aient été joués.

        Si le combat est terminé :
            - le vainqueur gagne 50 * (niveau du perdant) points d'expérience,
            - la ligne "<nom du vainqueur> remporte le combat" est ajoutée
              au journal,
            - retourne le vainqueur.
        Sinon, retourne None.
        """
        pass
