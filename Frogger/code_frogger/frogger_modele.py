
class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 1600
        self.hauteur = 900
        self.terrain = Terrain(self)

class Terrain():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = self.parent.largeur
        self.hauteur = self.parent.hauteur
        self.baie = Baie(self, 0, 10, "lightgreen")
        self.riviere = Riviere(self, 10, 40, "blue")
        self.plage = Plage(self, 40, 50, "wheat")
        self.rue = Rue(self, 50, 90, "gray50")
        self.gazon = Gazon(self, 90, 100, "green")

class Section_terrain():
    def __init__(self, parent, debut, fin, couleur):
        self.parent = parent
        self.hauteur = self.parent.hauteur/100
        self.haut = self.hauteur*debut
        self.bas = self.hauteur*fin
        self.couleur = couleur

class Baie(Section_terrain):
    def __init__(self, parent, debut, fin, couleur):
        super().__init__(parent, debut, fin, couleur)

class Riviere(Section_terrain):
    def __init__(self, parent, debut, fin, couleur):
        super().__init__(parent, debut, fin, couleur)
        self.courant = None

class Plage(Section_terrain):
    def __init__(self, parent, debut, fin, couleur):
        super().__init__(parent, debut, fin, couleur)

class Rue(Section_terrain):
    def __init__(self, parent, debut, fin, couleur):
        super().__init__(parent, debut, fin, couleur)
        self.voies = None

class Gazon(Section_terrain):
    def __init__(self, parent, debut, fin, couleur):
        super().__init__(parent, debut, fin, couleur)

