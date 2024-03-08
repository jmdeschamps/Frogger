import frogger_vue
import frogger_modele

class Controleur():
    def __init__(self):
        self.modele = frogger_modele.Modele(self)
        self.vue = frogger_vue.Vue(self,self.modele)
        self.vue.afficher_terrain()
        self.vue.root.mainloop()

if __name__ == "__main__":
    c = Controleur()
    print("In Frogger")