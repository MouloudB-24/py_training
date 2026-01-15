# ---- Symetric Difference ----

import json


def symtric_difference(*args):
    current_diff = args[0]
    for i in range(len(args)-1):
        current_diff = list(set(current_diff) ^ set(args[i+1]))
    return current_diff



#  sym([1, 2, 3], [5, 2, 1, 4]) should return [3, 4, 5]

# print(symtric_difference([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))

def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target, f"Value found at index {mid}"
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1
            
    return [], "Value not fount"


# print(binary_search([1, 2, 3, 4, 5], 3))
# print(binary_search([1, 2, 3, 4, 5, 9], 4))
# print(binary_search([1, 2, 3, 4, 5, 9, 10], 10))


"""
# ✔️ Implémenter le Bisection Method (méthode de bissection)

La bisection method (méthode de bissection) — aussi appelée binary search method (méthode de recherche binaire) — utilise une recherche binaire pour trouver la racine d’une fonction réelle.
L'idée est de réduire progressivement un intervalle dans lequel se trouve la racine, jusqu’à ce que la méthode converge vers une valeur qui respecte une tolerance (tolérance).

# 🎯 Principe de la méthode
Si la tolérance = 0.01, alors la méthode continue de diviser l’intervalle par deux jusqu’à ce que : upper_bound - lower_bound ≤ 0.01

# 🧪 Objectif du lab
Tu dois implémenter une fonction qui utilise la bisection method pour calculer la racine carrée d'un nombre.

# 📌 User Stories (exigences)

## 🔧 1. Définir une fonction

    Nom : square_root_bisection
    Paramètres :
    * number : le nombre dont on veut la racine carrée
    * tolerance (tolérance) : marge d’erreur acceptable (valeur par défaut)
    * max_iterations (nombre maximal d’itérations) : limite d’itérations (valeur par défaut)

## ✔️ 2. Comportements attendus de la fonction

    ### ❗ Cas négatif

    Si le nombre est négatif →
    ➡️ lever une ValueError avec le message :
    Square root of negative number is not defined in real numbers

    ### ✔️ Cas particuliers : 0 et 1

    Pour 0 et 1, afficher :
    The square root of [number] is [number]
    ➡️ Retourner directement le nombre.

    ### 🔍 Cas général : nombre positif

    * Calculer la racine carrée par bisection method.
    * Afficher :
    The square root of [square_target] is approximately [root]
    * Retourner la valeur obtenue.

    ### ❌ Cas où la méthode ne converge pas
    Si aucune valeur ne satisfait la tolérance :
    Afficher :
    Failed to converge within the [maximum] iterations
        ➡️ Retourner None

## ⚠️ Règle importante

➡️ Tu n’as pas le droit d’importer de module.

"""

def square_root_bisection(number: int, tolerance: float=0.01, max_iterations: int=100):
    
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number == 0:
        print("The square root of 0 is 0")
        return 0
        
    elif number < 1:
        root = number**0.5
        print(f"The square root of {number} is {root}")
        return root
    
    elif number == 1:
        print("The square root of 1 is 1")
        return 1
        
    else:    
        search_list = list(range(number))
        
        low = 0
        high = len(search_list)
        count = 1
        while count <= max_iterations:
            root = (low + high) / 2
            square_root = root**2
            
            if square_root > number:
                high = root - tolerance
            else:
                low = root + tolerance
            count += 1
                
        if high - low <= tolerance:
            print(f"The square root of {number} is approximately {root}")
            return root
        
        print(f"Failed to converge within {max_iterations} iterations")
        return None
    
# square_root_bisection(0.001, 1e-7, 50)


obj = {
    "organisation": "InnovTech Solutions",
    "dernière_mise_à_jour": "2025-05-10",
    "projets": [
        {
            "id": 101,
            "nom": "IA Santé",
            "description": "Développement d'une IA pour diagnostiquer les maladies rares.",
            "date_début": "2024-03-01",
            "date_fin": "",
            "statut": "en cours",
            "membres": [
                {
                    "nom": "Alice Dupont",
                    "rôle": "Chef de projet"
                },
                {
                    "nom": "Karim Bellarbi",
                    "rôle": "Développeur IA"
                }
            ],
            "technologies": [
                "Python",
                "TensorFlow",
                "FastAPI"
            ]
        },
        {
            "id": 102,
            "nom": "Plateforme Éducation",
            "description": "Plateforme en ligne pour la formation continue des enseignants.",
            "date_début": "2023-09-15",
            "date_fin": "2024-06-30",
            "statut": "terminé",
            "membres": [
                {
                    "nom": "Léa Martin",
                    "rôle": "Designer UX"
                },
                {
                    "nom": "Paul Nguyen",
                    "rôle": "Développeur Frontend"
                }
            ],
            "technologies": [
                "React",
                "Node.js",
                "MongoDB"
            ]
        }
    ]
}

def update_json(obj: json, target_name: str, new_job: str) -> None:
    """Algorithme intelligent pour modifier in JSON.
    """
    if isinstance(obj, dict):
        print("Je traite un Dict...")
        if obj.get("nom") == target_name:
            if "rôle" in obj:
                print(f"Trouvé {target_name} avec le rôle : {obj['rôle']}")
                obj["rôle"] = new_job
                print(f"Rôle modifié en : {new_job}")
                return
        
        for value in obj.values():
            update_json(value, target_name, new_job)
    
    elif isinstance(obj, list):
        print("Je traite une List...")
        for item in obj:
            update_json(item, target_name, new_job)


update_json(obj, "Alice Dupont", "Data Engineer")

