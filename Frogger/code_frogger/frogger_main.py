import frogger_vue
import frogger_modele

class Controleur():
    def __init__(self):
        self.modele = frogger_modele.Modele(self)
        self.vue = frogger_vue.Vue(self,self.modele)
        self.vue.afficher_frog()
        self.vue.root.mainloop()

    def frog_monter(self):
        self.modele.frog_monter()
        self.vue.afficher_frog()

if __name__ == "__main__":
    c = Controleur()
    print("In Frogger")