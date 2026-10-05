"""
Données de l'exercice 2 : NE PAS MODIFIER CE FICHIER.

ECOLE est une structure imbriquée qui mélange dict, list, tuple, set,
str, int, float, bool et None.
"""

ECOLE = {
    "nom": "Académie Python",
    "adresse": {
        "ville": "Lyon",
        "code_postal": "69001",
        "coordonnees": (45.76, 4.83),
    },
    "classes": [
        {
            "nom": "Débutants",
            "professeur": {
                "nom": "Martin",
                "contact": {
                    "email": "martin@academie-python.fr",
                    "telephones": ["06 11 22 33 44", "04 72 00 00 01"],
                },
            },
            "horaires": {
                "lundi": [("09:00", "12:00")],
                "jeudi": [("14:00", "17:00")],
            },
            "eleves": [
                {
                    "id": 1,
                    "prenom": "Alice",
                    "age": 19,
                    "actif": True,
                    "notes": {"python": [12, 15.5], "sql": [9]},
                    "options": {"sport", "cantine"},
                    "tuteur": None,
                },
                {
                    "id": 2,
                    "prenom": "Bilal",
                    "age": 22,
                    "actif": True,
                    "notes": {"python": [8, 10, 11]},
                    "options": {"cantine"},
                    "tuteur": {"nom": "Durand", "telephone": "06 55 44 33 22"},
                },
                {
                    "id": 3,
                    "prenom": "Chloé",
                    "age": 18,
                    "actif": False,
                    "notes": {"python": [], "sql": [14, 16]},
                    "options": set(),
                    "tuteur": None,
                },
            ],
        },
        {
            "nom": "Intermédiaires",
            "professeur": {
                "nom": "Nguyen",
                "contact": {
                    "email": "nguyen@academie-python.fr",
                    "telephones": ["06 98 76 54 32"],
                },
            },
            "horaires": {
                "mardi": [("09:00", "12:00"), ("13:30", "16:30")],
            },
            "eleves": [
                {
                    "id": 4,
                    "prenom": "David",
                    "age": 25,
                    "actif": True,
                    "notes": {"python": [16, 18], "sql": [13]},
                    "options": {"sport", "théâtre"},
                    "tuteur": None,
                },
                {
                    "id": 5,
                    "prenom": "Emma",
                    "age": 21,
                    "actif": True,
                    "notes": {"python": [14], "sql": [11, 12.5]},
                    "options": {"théâtre"},
                    "tuteur": {"nom": "Leroy", "telephone": "07 12 34 56 78"},
                },
            ],
        },
        {
            "nom": "Avancés",
            "professeur": {
                "nom": "Garcia",
                "contact": {
                    "email": "garcia@academie-python.fr",
                    "telephones": ["04 78 12 34 56", "06 00 11 22 33", "07 44 55 66 77"],
                },
            },
            "horaires": {
                "mercredi": [("08:30", "12:30")],
                "vendredi": [("14:00", "18:00")],
            },
            "eleves": [
                {
                    "id": 6,
                    "prenom": "Farid",
                    "age": 27,
                    "actif": True,
                    "notes": {"python": [19, 17.5, 20], "sql": [15]},
                    "options": {"sport", "cantine", "théâtre"},
                    "tuteur": None,
                },
                {
                    "id": 7,
                    "prenom": "Gaëlle",
                    "age": 24,
                    "actif": True,
                    "notes": {},
                    "options": {"cantine"},
                    "tuteur": None,
                },
                {
                    "id": 8,
                    "prenom": "Hugo",
                    "age": 30,
                    "actif": False,
                    "notes": {"python": [9.5], "sql": []},
                    "options": set(),
                    "tuteur": None,
                },
            ],
        },
    ],
}
