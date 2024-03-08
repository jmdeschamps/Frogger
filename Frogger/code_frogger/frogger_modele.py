
class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.terrain = None

class Terrain():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 800
        self.hauteur = 600
        self.gazon = Gazon(self,)
        self.rue = None
        self.plage = None
        self.riviere = None
        self.baie = None

class Gazon():
    def __init__(self, parent):
        self.parent = parent
        self.hauteur = self.parent.hauteur/10
        self.haut = self.hauteur/10*9
        self.bas = self.haut+self.hauteur
        self.couleur = "green"


class Rue():
    def __init__(self, parent):
        self.parent = parent
        self.hauteur = self.parent.hauteur/10*4
        self.haut = self.parent.hauteur/10*5
        self.bas = self.haut+self.hauteur
        self.couleur = "grey50"


class Plage():
    def __init__(self, parent):
        self.parent = parent
        self.hauteur = self.parent.hauteur/10
        self.haut = self.hauteur/10*4
        self.bas = self.haut+self.hauteur
        self.couleur = "wheat2"