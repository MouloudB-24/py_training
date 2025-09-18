class Toolbox:
    """Boite à utils"""

    def __init__(self):
        """Initialiser les outils."""
        self.tools = []  # commentaire

    def add_tool(self, tool):
        """Ajouter un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enlever un outil?"""
        index = self.tools.index(tool)
        del self.tools[index]


class Hammer:
    """Marteau"""

    def __init__(self, color: str = "red"):
        """Iinitialise la couleur."""
        self.color = color

    def paint(self, color):
        """Paint le marteau."""
        self.color = color

    def hammer_in(self, nail):
        """Enfoncez un clous."""
        nail.nail_in()

    def remove(self, nail):
        """Enlevez un clous."""
        nail.remove()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"


class Screwdriver:
    """Tournevis"""

    def __init__(self, size: int = 3):
        """Initialise la taille."""
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()

    def loosen(self, screw):
        """Desserer une vis."""
        screw.loosen()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"


class Screw:
    """Vis."""

    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0

    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""

    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False

    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."


# Instanciez une boîte à outils, un tournevis, et un marteau.
boite_a_outils = Toolbox()
tournevis = Screwdriver()
marteau = Hammer()

# Placez le marteau et le tournevis dans la boîte à outils.
boite_a_outils.add_tool(tournevis)
boite_a_outils.add_tool(marteau)

# Instanciez une vis, et serrez-la avec le tournevis. Affichez la vis avant et après avoir été serrée.
vis = Screw()
print(vis)
tournevis.tighten(vis)
print(vis)

# Instanciez un clou, puis enfoncez-le avec le marteau. Affichez le clou avant et après avoir été enfoncé.
clou = Nail()
print(clou)
marteau.hammer_in(clou)
print(clou)
