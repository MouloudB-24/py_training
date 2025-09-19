# Problem : Traveling Salesman
from math import sqrt
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
       cities.append(tuple(city.split()))
    return cities


def calculate_distance(city1, city2):
    return sqrt((float(city1[1]) - float(city2[1]))**2 + (float(city1[2]) - float(city2[2]))**2) 


if __name__ == "__main__":
    cities = load_cities("data/villes.txt")
    print(f"The number of cities is:  {len(cities)}\n")
    print("Here are the first 10 on the list:")
    print(cities[:10])
    
    paris_bordeaux = calculate_distance(cities[0], cities[1])
    print(f"\nDistance entre Paris et Bordeaux est : {paris_bordeaux}")
    paris_bordeaux = calculate_distance(cities[1], cities[2])
    print(f"Distance entre Bordeaux et Marseille est : {paris_bordeaux}")