"""
Tests de l'exercice 1.

Lancement :  pytest test_exercise.py -v
"""

import pytest

from exercise import analyser_notes, categoriser_temperature, compter_voyelles


# ---------------------------------------------------------------------------
# Partie 1 : categoriser_temperature
# ---------------------------------------------------------------------------
class TestCategoriserTemperature:
    @pytest.mark.parametrize(
        "temperature, attendu",
        [
            (-20, "glacial"),
            (-0.5, "glacial"),
            (0, "froid"),
            (8, "froid"),
            (14.9, "froid"),
            (15, "doux"),
            (20.3, "doux"),
            (24.99, "doux"),
            (25, "chaud"),
            (42, "chaud"),
        ],
    )
    def test_categories(self, temperature, attendu):
        assert categoriser_temperature(temperature) == attendu, (
            f"categoriser_temperature({temperature!r}) devrait retourner {attendu!r}"
        )

    @pytest.mark.parametrize("valeur", ["20", None, [10], True, False])
    def test_valeur_invalide(self, valeur):
        assert categoriser_temperature(valeur) == "invalide", (
            f"{valeur!r} n'est pas une température valide"
        )

    def test_retourne_une_chaine(self):
        assert isinstance(categoriser_temperature(10), str)


# ---------------------------------------------------------------------------
# Partie 2 : compter_voyelles
# ---------------------------------------------------------------------------
def voyelles(a=0, e=0, i=0, o=0, u=0, y=0):
    return {"a": a, "e": e, "i": i, "o": o, "u": u, "y": y}


class TestCompterVoyelles:
    def test_retourne_un_dict(self):
        assert isinstance(compter_voyelles("abc"), dict)

    def test_texte_vide(self):
        assert compter_voyelles("") == voyelles()

    def test_mot_simple(self):
        assert compter_voyelles("Bonjour") == voyelles(o=2, u=1)

    def test_toutes_les_cles_presentes(self):
        assert set(compter_voyelles("xyz").keys()) == {"a", "e", "i", "o", "u", "y"}

    def test_sans_voyelle(self):
        assert compter_voyelles("bcdfg 123 !?") == voyelles()

    def test_majuscules(self):
        assert compter_voyelles("AEIOUY aeiouy") == voyelles(2, 2, 2, 2, 2, 2)

    def test_phrase(self):
        assert compter_voyelles("Python est super") == voyelles(e=2, o=1, u=1, y=1)

    def test_accents_ignores(self):
        assert compter_voyelles("été à Noël") == voyelles(o=1)

    def test_repetitions(self):
        assert compter_voyelles("aaaaa") == voyelles(a=5)


# ---------------------------------------------------------------------------
# Partie 3 : analyser_notes
# ---------------------------------------------------------------------------
AUCUNE_NOTE = {
    "moyenne": 0.0,
    "admis": 0,
    "recales": 0,
    "meilleure": None,
    "mention": "Aucune note",
}


class TestAnalyserNotes:
    def test_retourne_un_dict_avec_les_bonnes_cles(self):
        resultat = analyser_notes([10])
        assert isinstance(resultat, dict)
        assert set(resultat.keys()) == {"moyenne", "admis", "recales", "meilleure", "mention"}

    def test_liste_vide(self):
        assert analyser_notes([]) == AUCUNE_NOTE

    def test_que_des_valeurs_invalides(self):
        assert analyser_notes(["abc", None, -1, 21, True]) == AUCUNE_NOTE

    def test_exemple_simple(self):
        assert analyser_notes([12, 8, 15.5]) == {
            "moyenne": 11.83,
            "admis": 2,
            "recales": 1,
            "meilleure": 15.5,
            "mention": "Passable",
        }

    def test_valeurs_invalides_ignorees(self):
        assert analyser_notes([10, "abc", 25, -3, 14]) == {
            "moyenne": 12.0,
            "admis": 2,
            "recales": 0,
            "meilleure": 14,
            "mention": "Assez bien",
        }

    def test_bornes_0_et_20_valides(self):
        resultat = analyser_notes([0, 20])
        assert resultat["moyenne"] == 10.0
        assert resultat["admis"] == 1
        assert resultat["recales"] == 1
        assert resultat["meilleure"] == 20

    def test_booleen_ignore(self):
        assert analyser_notes([True, 12])["moyenne"] == 12.0

    def test_note_10_est_admise(self):
        resultat = analyser_notes([10, 9.99])
        assert resultat["admis"] == 1
        assert resultat["recales"] == 1

    @pytest.mark.parametrize(
        "notes, mention",
        [
            ([18, 16], "Très bien"),
            ([16], "Très bien"),
            ([14, 15], "Bien"),
            ([12, 13.5], "Assez bien"),
            ([10, 11], "Passable"),
            ([5, 9], "Insuffisant"),
        ],
    )
    def test_mentions(self, notes, mention):
        assert analyser_notes(notes)["mention"] == mention

    def test_moyenne_arrondie(self):
        assert analyser_notes([10, 10, 11])["moyenne"] == 10.33
