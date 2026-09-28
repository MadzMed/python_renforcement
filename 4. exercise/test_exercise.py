"""
Tests de l'exercice 4.

Lancement :  pytest test_exercise.py -v
"""

import inspect
from abc import ABC

import pytest

from rpg import ActionImpossible, Archer, Combat, Guerrier, Inventaire, Mage, Objet, Personnage


@pytest.fixture(autouse=True)
def remise_a_zero_compteur():
    Personnage.nombre_personnages = 0


def attribut_de(classe, nom):
    """Retourne l'attribut tel qu'il est défini dans la classe (sans héritage)."""
    return inspect.getattr_static(classe, nom, None)


# ===========================================================================
# Partie 1 : exception, objets et inventaire
# ===========================================================================
class TestPartie1Exception:
    def test_herite_de_exception(self):
        assert issubclass(ActionImpossible, Exception)

    def test_peut_etre_levee(self):
        with pytest.raises(ActionImpossible):
            raise ActionImpossible("interdit")


class TestPartie1Objet:
    def test_attributs(self):
        potion = Objet("Potion", "soin", 30)
        assert potion.nom == "Potion"
        assert potion.type == "soin"
        assert potion.valeur == 30

    def test_repr(self):
        assert repr(Objet("Épée", "arme", 5)) == "Objet('Épée', 'arme', 5)"

    def test_type_invalide(self):
        with pytest.raises(ValueError):
            Objet("Pomme", "nourriture", 3)


class TestPartie1Inventaire:
    def test_vide_au_depart(self):
        sac = Inventaire()
        assert sac.capacite == 5
        assert sac.objets == []
        assert len(sac) == 0

    def test_capacite_personnalisee(self):
        assert Inventaire(2).capacite == 2

    def test_ajouter_et_contains(self):
        sac = Inventaire()
        sac.ajouter(Objet("Potion", "soin", 30))
        assert len(sac) == 1
        assert "Potion" in sac
        assert "Épée" not in sac

    def test_inventaire_plein(self):
        sac = Inventaire(2)
        sac.ajouter(Objet("Potion", "soin", 30))
        sac.ajouter(Objet("Potion", "soin", 30))
        with pytest.raises(ActionImpossible):
            sac.ajouter(Objet("Épée", "arme", 5))
        assert len(sac) == 2

    def test_retirer_retourne_l_objet(self):
        sac = Inventaire()
        epee = Objet("Épée", "arme", 5)
        sac.ajouter(Objet("Potion", "soin", 30))
        sac.ajouter(epee)
        assert sac.retirer("Épée") is epee
        assert len(sac) == 1
        assert "Épée" not in sac

    def test_retirer_un_seul_exemplaire(self):
        sac = Inventaire()
        sac.ajouter(Objet("Potion", "soin", 30))
        sac.ajouter(Objet("Potion", "soin", 30))
        sac.retirer("Potion")
        assert len(sac) == 1
        assert "Potion" in sac

    def test_retirer_absent(self):
        with pytest.raises(ActionImpossible):
            Inventaire().retirer("Potion")

    def test_deux_inventaires_independants(self):
        a, b = Inventaire(), Inventaire()
        a.ajouter(Objet("Potion", "soin", 30))
        assert len(b) == 0


# ===========================================================================
# Partie 2 : Personnage (classe abstraite, encapsulation, méthodes spéciales)
# ===========================================================================
class TestPartie2Abstraction:
    def test_personnage_est_abstrait(self):
        assert issubclass(Personnage, ABC)
        assert inspect.isabstract(Personnage)

    def test_impossible_d_instancier_personnage(self):
        with pytest.raises(TypeError):
            Personnage("Bob")

    def test_attaquer_est_abstraite(self):
        assert "attaquer" in Personnage.__abstractmethods__

    def test_classe_fille_sans_attaquer(self):
        class Incomplet(Personnage):
            pass

        with pytest.raises(TypeError):
            Incomplet("Bob")


class TestPartie2AttributsDeClasse:
    def test_valeurs_par_defaut(self):
        assert Personnage.PV_BASE == 100
        assert Personnage.ATTAQUE_BASE == 10
        assert Personnage.DEFENSE_BASE == 0

    def test_compteur(self):
        Guerrier("A")
        Mage("B")
        Archer("C")
        assert Personnage.nombre_personnages == 3

    def test_compteur_partage(self):
        Guerrier("A")
        Guerrier("B")
        # Le compteur doit être celui de Personnage, pas un attribut par classe.
        assert "nombre_personnages" not in Guerrier.__dict__
        assert Personnage.nombre_personnages == 2


class TestPartie2Initialisation:
    def test_attributs_de_depart(self):
        g = Guerrier("Aragorn")
        assert g.nom == "Aragorn"
        assert g.niveau == 1
        assert g.experience == 0
        assert g.pv_max == 120
        assert g.pv == 120
        assert g.attaque == 15
        assert g.defense == 5

    def test_inventaire_composition(self):
        g1, g2 = Guerrier("A"), Guerrier("B")
        assert isinstance(g1.inventaire, Inventaire)
        assert g1.inventaire is not g2.inventaire


class TestPartie2Encapsulation:
    def test_pv_est_une_propriete(self):
        assert isinstance(attribut_de(Personnage, "pv"), property)

    def test_pv_stocke_dans_attribut_prive(self):
        g = Guerrier("Aragorn")
        assert g._pv == 120
        g.pv = 50
        assert g._pv == 50

    def test_pv_borne_en_bas(self):
        g = Guerrier("Aragorn")
        g.pv = -50
        assert g.pv == 0

    def test_pv_borne_en_haut(self):
        g = Guerrier("Aragorn")
        g.pv = 9999
        assert g.pv == 120

    def test_est_vivant(self):
        g = Guerrier("Aragorn")
        assert g.est_vivant is True
        g.pv = 0
        assert g.est_vivant is False

    def test_est_vivant_lecture_seule(self):
        assert isinstance(attribut_de(Personnage, "est_vivant"), property)
        with pytest.raises(AttributeError):
            Guerrier("Aragorn").est_vivant = False


class TestPartie2Methodes:
    def test_subir_degats(self):
        g = Guerrier("Aragorn")
        assert g.subir_degats(20) == 15
        assert g.pv == 105

    def test_subir_degats_minimum_1(self):
        g = Guerrier("Aragorn")
        assert g.subir_degats(2) == 1
        assert g.pv == 119

    def test_subir_degats_pv_jamais_negatifs(self):
        g = Guerrier("Aragorn")
        g.subir_degats(500)
        assert g.pv == 0
        assert g.est_vivant is False

    def test_soigner(self):
        g = Guerrier("Aragorn")
        g.pv = 50
        assert g.soigner(30) == 30
        assert g.pv == 80

    def test_soigner_plafonne(self):
        g = Guerrier("Aragorn")
        g.pv = 100
        assert g.soigner(50) == 20
        assert g.pv == 120

    def test_soigner_un_mort(self):
        g = Guerrier("Aragorn")
        g.pv = 0
        with pytest.raises(ActionImpossible):
            g.soigner(10)

    def test_utiliser_potion(self):
        g = Guerrier("Aragorn")
        g.pv = 50
        g.inventaire.ajouter(Objet("Potion", "soin", 30))
        g.utiliser_objet("Potion")
        assert g.pv == 80
        assert "Potion" not in g.inventaire

    def test_utiliser_arme(self):
        g = Guerrier("Aragorn")
        g.inventaire.ajouter(Objet("Épée", "arme", 5))
        g.utiliser_objet("Épée")
        assert g.attaque == 20
        assert len(g.inventaire) == 0

    def test_utiliser_objet_absent(self):
        with pytest.raises(ActionImpossible):
            Guerrier("Aragorn").utiliser_objet("Potion")

    def test_utiliser_objet_mort_garde_l_objet(self):
        g = Guerrier("Aragorn")
        g.inventaire.ajouter(Objet("Potion", "soin", 30))
        g.pv = 0
        with pytest.raises(ActionImpossible):
            g.utiliser_objet("Potion")
        assert "Potion" in g.inventaire


class TestPartie2Niveaux:
    def test_xp_pour_niveau_statique(self):
        assert isinstance(attribut_de(Personnage, "xp_pour_niveau"), staticmethod)
        assert Personnage.xp_pour_niveau(1) == 100
        assert Personnage.xp_pour_niveau(3) == 300
        assert Guerrier("A").xp_pour_niveau(2) == 200

    def test_pas_assez_d_experience(self):
        g = Guerrier("Aragorn")
        assert g.gagner_experience(99) == 0
        assert g.niveau == 1
        assert g.experience == 99

    def test_un_niveau(self):
        g = Guerrier("Aragorn")
        assert g.gagner_experience(250) == 1
        assert g.niveau == 2
        assert g.experience == 150

    def test_plusieurs_niveaux(self):
        g = Guerrier("Aragorn")
        assert g.gagner_experience(350) == 2
        assert g.niveau == 3
        assert g.experience == 50

    def test_monter_niveau_ameliore_les_stats(self):
        g = Guerrier("Aragorn")
        g.pv = 10
        g.monter_niveau()
        assert g.niveau == 2
        assert g.pv_max == 130
        assert g.pv == 130
        assert g.attaque == 17
        assert g.defense == 6


class TestPartie2MethodeDeClasse:
    def test_est_une_methode_de_classe(self):
        assert isinstance(attribut_de(Personnage, "depuis_dict"), classmethod)

    def test_depuis_dict_guerrier(self):
        g = Guerrier.depuis_dict({"nom": "Aragorn", "niveau": 3})
        assert type(g) is Guerrier
        assert g.nom == "Aragorn"
        assert g.niveau == 3
        assert g.pv_max == 140

    def test_depuis_dict_mage(self):
        m = Mage.depuis_dict({"nom": "Merlin", "niveau": 2})
        assert type(m) is Mage
        assert m.mana_max == 60

    def test_depuis_dict_niveau_par_defaut(self):
        a = Archer.depuis_dict({"nom": "Legolas"})
        assert type(a) is Archer
        assert a.niveau == 1


class TestPartie2MethodesSpeciales:
    def test_str(self):
        g = Guerrier("Aragorn")
        assert str(g) == "Aragorn (Guerrier) - niveau 1 - PV 120/120"
        g.pv = 42
        assert str(g) == "Aragorn (Guerrier) - niveau 1 - PV 42/120"

    def test_str_mage(self):
        assert str(Mage("Merlin")) == "Merlin (Mage) - niveau 1 - PV 80/80"

    def test_repr(self):
        assert repr(Archer("Legolas")) == "Archer('Legolas', niveau=1)"

    def test_egalite(self):
        assert Guerrier("Aragorn") == Guerrier("Aragorn")

    def test_egalite_niveau_different(self):
        g = Guerrier("Aragorn")
        g.monter_niveau()
        assert g != Guerrier("Aragorn")

    def test_egalite_classe_differente(self):
        assert Guerrier("Bob") != Archer("Bob")

    def test_egalite_autre_type(self):
        assert Guerrier("Bob") != "Bob"

    def test_tri_par_niveau(self):
        a = Guerrier.depuis_dict({"nom": "A", "niveau": 3})
        b = Mage.depuis_dict({"nom": "B", "niveau": 1})
        c = Archer.depuis_dict({"nom": "C", "niveau": 2})
        assert b < c < a
        assert [p.nom for p in sorted([a, b, c])] == ["B", "C", "A"]


# ===========================================================================
# Partie 3 : héritage et polymorphisme
# ===========================================================================
class TestPartie3Heritage:
    @pytest.mark.parametrize("classe", [Guerrier, Mage, Archer])
    def test_herite_de_personnage(self, classe):
        assert issubclass(classe, Personnage)
        assert isinstance(classe("X"), Personnage)

    @pytest.mark.parametrize(
        "classe, pv, attaque, defense",
        [(Guerrier, 120, 15, 5), (Mage, 80, 8, 2), (Archer, 100, 12, 3)],
    )
    def test_statistiques(self, classe, pv, attaque, defense):
        assert classe.PV_BASE == pv
        perso = classe("X")
        assert (perso.pv_max, perso.pv, perso.attaque, perso.defense) == (pv, pv, attaque, defense)

    @pytest.mark.parametrize("classe", [Guerrier, Mage, Archer])
    def test_redefinit_attaquer(self, classe):
        assert issubclass(classe, Personnage)
        assert "attaquer" in classe.__dict__
        assert classe.attaquer is not Personnage.attaquer

    def test_mage_utilise_super(self):
        m = Mage("Merlin")
        # Les attributs du parent ET ceux du mage doivent exister.
        assert m.niveau == 1
        assert isinstance(m.inventaire, Inventaire)
        assert m.mana_max == 50
        assert m.mana == 50

    def test_archer_utilise_super(self):
        a = Archer("Legolas")
        assert a.niveau == 1
        assert a.nombre_tirs == 0


class TestPartie3Polymorphisme:
    def test_meme_appel_resultats_differents(self):
        attaquants = [Guerrier("G"), Mage("M"), Archer("A")]
        degats = [perso.attaquer(Guerrier("Cible")) for perso in attaquants]
        # Guerrier : 15 - 5 ; Mage (boule de feu) : 24 - 5 ; Archer : 12 - 5
        assert degats == [10, 19, 7]


class TestPartie3Guerrier:
    def test_attaque_normale(self):
        cible = Archer("Cible")
        assert Guerrier("G").attaquer(cible) == 12
        assert cible.pv == 88

    def test_rage(self):
        g = Guerrier("G")
        g.pv = 35  # 35 < 36 (30 % de 120)
        assert g.attaquer(Archer("Cible")) == 27

    def test_pas_de_rage_a_30_pourcent(self):
        g = Guerrier("G")
        g.pv = 36  # pile 30 % : pas de rage
        assert g.attaquer(Archer("Cible")) == 12


class TestPartie3Mage:
    def test_boule_de_feu(self):
        m = Mage("M")
        assert m.attaquer(Archer("Cible")) == 21
        assert m.mana == 40

    def test_sans_mana(self):
        m = Mage("M")
        m.mana = 9
        assert m.attaquer(Archer("Cible")) == 5
        assert m.mana == 9

    def test_cinq_sorts_puis_attaque_normale(self):
        m = Mage("M")
        cible = Guerrier("Cible")
        degats = [m.attaquer(cible) for _ in range(6)]
        assert degats == [19, 19, 19, 19, 19, 3]
        assert m.mana == 0

    def test_monter_niveau_etend_le_parent(self):
        m = Mage("M")
        m.mana = 0
        m.monter_niveau()
        assert m.niveau == 2
        assert m.pv_max == 90
        assert m.attaque == 10
        assert m.mana_max == 60
        assert m.mana == 60

    def test_monter_niveau_par_l_experience(self):
        m = Mage("M")
        m.gagner_experience(100)
        assert m.mana_max == 60


class TestPartie3Archer:
    def test_tir_critique_tous_les_3_tirs(self):
        a = Archer("A")
        cible = Guerrier("Cible")
        degats = [a.attaquer(cible) for _ in range(6)]
        assert degats == [7, 7, 19, 7, 7, 19]
        assert a.nombre_tirs == 6


class TestPartie3AttaquesImpossibles:
    @pytest.mark.parametrize("classe", [Guerrier, Mage, Archer])
    def test_cible_morte(self, classe):
        cible = Guerrier("Cible")
        cible.pv = 0
        with pytest.raises(ActionImpossible):
            classe("X").attaquer(cible)

    @pytest.mark.parametrize("classe", [Guerrier, Mage, Archer])
    def test_attaquant_mort(self, classe):
        perso = classe("X")
        perso.pv = 0
        with pytest.raises(ActionImpossible):
            perso.attaquer(Guerrier("Cible"))

    @pytest.mark.parametrize("classe", [Guerrier, Mage, Archer])
    def test_s_attaquer_soi_meme(self, classe):
        perso = classe("X")
        with pytest.raises(ActionImpossible):
            perso.attaquer(perso)


# ===========================================================================
# Partie 4 : le combat
# ===========================================================================
class TestPartie4Combat:
    def test_creation(self):
        g, m = Guerrier("Aragorn"), Mage("Merlin")
        combat = Combat(g, m)
        assert combat.p1 is g
        assert combat.p2 is m
        assert combat.journal == []
        assert combat.nombre_tours == 0
        assert combat.est_termine is False
        assert combat.vainqueur is None

    def test_meme_personnage(self):
        g = Guerrier("Aragorn")
        with pytest.raises(ActionImpossible):
            Combat(g, g)

    def test_personnage_mort(self):
        m = Mage("Merlin")
        m.pv = 0
        with pytest.raises(ActionImpossible):
            Combat(Guerrier("Aragorn"), m)

    def test_un_tour(self):
        g, m = Guerrier("Aragorn"), Mage("Merlin")
        combat = Combat(g, m)
        combat.tour()
        assert m.pv == 67
        assert g.pv == 101
        assert combat.nombre_tours == 1
        assert combat.journal == [
            "Aragorn inflige 13 dégâts à Merlin",
            "Merlin inflige 19 dégâts à Aragorn",
        ]

    def test_pas_de_riposte_si_mort(self):
        g, m = Guerrier("Aragorn"), Mage("Merlin")
        m.pv = 5
        combat = Combat(g, m)
        combat.tour()
        assert g.pv == 120
        assert len(combat.journal) == 1
        assert combat.est_termine is True
        assert combat.vainqueur is g

    def test_tour_apres_la_fin(self):
        g, m = Guerrier("Aragorn"), Mage("Merlin")
        m.pv = 5
        combat = Combat(g, m)
        combat.tour()
        with pytest.raises(ActionImpossible):
            combat.tour()

    def test_combat_complet(self):
        g, m = Guerrier("Aragorn"), Mage("Merlin")
        combat = Combat(g, m)
        vainqueur = combat.lancer()
        # 5 tours complets, puis au 6e tour le guerrier (en rage) achève le mage.
        assert vainqueur is g
        assert combat.nombre_tours == 6
        assert m.pv == 0
        assert g.pv == 25
        assert len(combat.journal) == 12
        assert combat.journal[-2] == "Aragorn inflige 28 dégâts à Merlin"
        assert combat.journal[-1] == "Aragorn remporte le combat"

    def test_experience_du_vainqueur(self):
        g = Guerrier("Aragorn")
        m = Mage.depuis_dict({"nom": "Merlin", "niveau": 1})
        Combat(g, m).lancer()
        assert g.experience == 50

    def test_experience_selon_niveau_du_perdant(self):
        a = Archer.depuis_dict({"nom": "Legolas", "niveau": 5})
        m = Mage.depuis_dict({"nom": "Merlin", "niveau": 3})
        vainqueur = Combat(a, m).lancer()
        assert vainqueur is a
        # 150 XP : niveau 5 demande 500 XP, donc pas de niveau gagné
        assert a.experience == 150
        assert a.niveau == 5

    def test_victoire_de_p2(self):
        a, g = Archer("Legolas"), Guerrier.depuis_dict({"nom": "Aragorn", "niveau": 4})
        assert Combat(a, g).lancer() is g

    def test_max_tours(self):
        g, m = Guerrier("Aragorn"), Mage("Merlin")
        combat = Combat(g, m)
        assert combat.lancer(max_tours=2) is None
        assert combat.nombre_tours == 2
        assert combat.est_termine is False
        assert g.experience == 0
