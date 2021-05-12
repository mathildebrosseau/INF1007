class Noeud(object):
    def __init__(self, nom):
        # TODO: à implémenter
        self.__nom = nom
        self.__voisins = []

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def voisins(self):
        return self.__voisins

    @voisins.setter
    def voisins(self, voisins):
        self.__voisins = voisins
    
    def ajoute_voisin(self, noeud):
        # TODO: à implémenter
        self.voisins.append(noeud)

    def __str__(self):
        # TODO: à implémenter
        return f"{self.nom} est connecté à {', '.join(voisin.nom for voisin in self.voisins)}"
    
    def __repr__(self):
        # TODO: à implémenter
        return self.nom


class Graphe(object):
    def __init__(self):
        # TODO: à implémenter
        self.graphe = []
                
    def ajoute_noeud(self, noeud: Noeud, aretes: list):
        # TODO: à implémenter
        if noeud not in self.graphe:
            for i in range(len(aretes)):
                noeud.ajoute_voisin(aretes[i])
            self.graphe.append(noeud)

    def ajoute_arete(self, noeud1: Noeud, noeud2: Noeud):
        # TODO: à implémenter
        noeud1.ajoute_voisin(noeud2)

    def trouve_chemin(self, debut: Noeud, fin: Noeud, chemin=None):
        # TODO: à implémenter
        if chemin is None:
            chemin = []

        if fin in debut.voisins:
            chemin.append(debut)
            chemin.append(fin)
            return chemin

        chemin.append(debut)
        for voisin in debut.voisins:
            debut = voisin
            graphe.trouve_chemin(debut, fin, chemin=chemin)
            return chemin


if __name__ == "__main__":
    # Création des noeuds
    a, b, c, d, e = Noeud('A'), Noeud('B'), Noeud('C'), Noeud('D'), Noeud('E')

    # Création du graphe
    graphe = Graphe()

    # Ajout des noeuds et des arêtes au graphe
    graphe.ajoute_noeud(noeud=a, aretes=[b, d])
    graphe.ajoute_noeud(noeud=b, aretes=[c])
    graphe.ajoute_noeud(noeud=c, aretes=[d, e])
    graphe.ajoute_noeud(noeud=d, aretes=[a, c, e])
    graphe.ajoute_noeud(noeud=e, aretes=[d])

    # Affichage de quelques noeuds
    print(a)
    print(d)
    print(e)

    # Recherche d'un chemin entre le noeud B et le noeud A
    chemin = graphe.trouve_chemin(b, a)
    print(f'Le chemin entre B et A est {chemin}')

    # Recherche d'un chemin entre le noeud E et le noeud B
    chemin = graphe.trouve_chemin(e, b)
    print(f'Le chemin entre E et B est {chemin}')

    # Recherche d'un chemin entre le noeud E et le noeud A
    chemin = graphe.trouve_chemin(e, c)
    print(f'Le chemin entre E et B est {chemin}')
