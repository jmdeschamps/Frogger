import tkinter
from tkinter import *

class Vue():
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.title("Frogger 2024")
        self.chercher_images()
        self.afficher_terrain()
        self.afficher_frog()

    def chercher_images(self):
        self.modele.frog.img_h = PhotoImage(file="./images/frog_h.png")

    def afficher_terrain(self):
        self.canevas = Canvas(self.root, width = self.modele.largeur,
                              height=self.modele.hauteur)
        obj = self.modele.terrain.baie
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, tags = ("statique",), fill=obj.couleur)
        obj = self.modele.terrain.riviere
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, tags = ("statique",), fill=obj.couleur)
        obj = self.modele.terrain.plage
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, tags = ("statique",), fill=obj.couleur)
        obj = self.modele.terrain.rue
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, tags = ("statique",), fill=obj.couleur)
        obj = self.modele.terrain.gazon
        self.canevas.create_rectangle(0, obj.haut, self.modele.largeur,
                                      obj.bas, tags = ("statique",), fill=obj.couleur)
        self.canevas.bind("<Up>",self.frog_monter)
        self.canevas.focus_set()
        self.canevas.pack()

    def frog_monter(self,evt):
        self.parent.frog_monter()

    def afficher_frog(self):
        self.canevas.delete("frog")
        frog = self.modele.frog
        x = self.modele.largeur/100*frog.position[0]
        y = self.modele.hauteur/100*frog.position[1]
        self.canevas.create_image(x,y,anchor="center",image=frog.img_h,
                                  tags=("dynamique","frog"))
