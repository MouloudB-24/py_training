# Problem : Traveling Salesman
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


if __name__ == "__main__":
    from pprint import pprint
    cities = load_cities("data/villes.txt")
    print(f"The number of cities is:  {len(cities)}\n")
    print("Here are the first 10 on the list:")
    pprint(cities[:10])