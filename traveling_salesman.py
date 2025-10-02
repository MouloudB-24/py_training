# Problem : Traveling Salesman
from math import sqrt
import math
from typing import List, Tuple


def load_cities(file: str) -> List[Tuple]:
    """Load cities from a text file and return them as a list of tuples.

    Args:
        file (str): path that points to the test file

    Returns:
        List[Tuple]: list of tuples containing city data
           
    >>> Example
    "paris 100, 220" -> [(paris, 100, 220)]
    """
    with open(file, "r", encoding="utf-8") as f:   
        raw_data = f.readlines()
    cities = []
    for city in raw_data:
        temp = city.strip().split()
        if len(temp) == 3:
            name, x, y = city.split()
        else:
            x, y = temp[-2], temp[-1]
            name = " ".join(temp[:-2])
        cities.append((name, float(x), float(y)))
    return cities


def get_distance_between_two_cities(city1, city2):
    return math.sqrt((city1[-2] - city2[-2])**2 + (city1[-1] - city2[-1])**2)


def get_itineraire_greedy(cities):
    itineraire = []
    i = 1
    while len(cities) > 1:
        visited_city = cities.pop(0)
        itineraire.append(visited_city)
        distance_min = float("inf")
        next_city = ""
        for city in cities:
            current_distance = get_distance_between_two_cities(visited_city, city)
            if current_distance < distance_min:
                distance_min = current_distance
                next_city = city
        cities.remove(next_city)
        cities.insert(0, next_city)
    itineraire += cities
    return itineraire 


def get_distance_total(itineraire):
    distance_tot = 0
    for i in range(len(itineraire)-1):
        distance_tot += get_distance_between_two_cities(itineraire[i], itineraire[i+1])
    return distance_tot


cities = load_cities("data/villes.txt")
print(f"The number of cities is:  {len(cities)}\n")

paris_bordeaux = get_distance_between_two_cities(cities[0], cities[1])
print(f"Distance entre Paris et Bordeaux est : {paris_bordeaux}")
paris_bordeaux = get_distance_between_two_cities(cities[1], cities[2])
print(f"Distance entre Bordeaux et Marseille est : {paris_bordeaux}")

# Calcul l'itineraire la plus court
itineraire = get_itineraire_greedy(cities)
print(itineraire[:10])

# Distance totale :
distance_tot = get_distance_total(itineraire)
print(f"\nLa distance totale de l'itineraire est : {distance_tot}")


