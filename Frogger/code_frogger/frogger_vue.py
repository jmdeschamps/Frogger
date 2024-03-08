from tkinter import *

class Vue():
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.title("Frogger 2024")

    def afficher_terrain(self):
        self.canevas = Canvas(self.root, width = self.modele.largeur,
                              height=self.modele.hauteur)
        obj = self.modele.terrain.baie
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, fill=obj.couleur)
        obj = self.modele.terrain.riviere
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, fill=obj.couleur)
        obj = self.modele.terrain.plage
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, fill=obj.couleur)
        obj = self.modele.terrain.rue
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, fill=obj.couleur)
        obj = self.modele.terrain.gazon
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, fill=obj.couleur)

        self.canevas.pack()