import random
import time
import threading


class AntColony:
    def __init__(self, distances : list, n_fourmis : int, n_meilleurs : int, n_iterations : int, decroissance : float, alpha : float = 1, beta : float = 2):
        """
        Initialise la colonie de fourmis.
        
        Paramètres :
        - distances : matrice des distances entre les villes ex : distances[i][j] est la distance entre la ville i et la ville j
        - n_fourmis : nombre de fourmis par itération
        - n_meilleurs : nombre de meilleurs chemins qui déposent des phéromones
        - n_iterations : nombre d'itérations de l'algorithme
        - decay : taux d'évaporation des phéromones (entre 0 et 1)
        - alpha : importance des phéromones (α)
        - beta : importance de l'heuristique (β)
        """
        self.distances = distances
        self.pheromones = [[1.0 for _ in range(len(distances))] for _ in range(len(distances))]
        self.n_fourmis = n_fourmis
        self.n_meilleurs = n_meilleurs
        self.n_iterations = n_iterations
        self.decroissance = decroissance
        self.alpha = alpha
        self.beta = beta

        # Liste de tous les indices des villes ex : 0, 1, 2, ..., n-1
        self.tous_indices = range(len(distances))

        # Variables pour stocker le meilleur chemin et la meilleure distance
        self.meilleur_chemin = None
        self.meilleure_distance = float('inf')
        
        self.it=0

    def run(self, callback_maj, evenement_arret):
        """
        Exécute l'algorithme d'optimisation par colonie de fourmis.

        Paramètres
        ----------
        callback_maj : callable
            Une fonction de callback à appeler après chaque itération.
            La fonction doit prendre trois paramètres : l'itération actuelle,
            le meilleur chemin trouvé jusqu'à présent, et la matrice des phéromones.
        evenement_arret : threading.Event
            Un événement à définir pour arrêter l'algorithme.

        Retourne
        -------
        None
        """
        self.it+=1
        list=self.generer_tous_chemins()
        tri=sorted(list, key=lambda x:x[1])
        chem,dist=tri[0]
        if dist<self.meilleure_distance:
            self.meilleure_distance=dist
            self.meilleur_chemin=chem
        self.deposer_pheromones(list)
        self.evaporer_pheromones()
        callback_maj(self.it,self.meilleur_chemin,self.pheromones)



    
    def calculer_distance_chemin(self, chemin):
        """
        Calcule la distance totale d'un chemin.

        Paramètres
        ----------
        chemin : list
            Une liste d'indices représentant un chemin.
        Retourne
        -------
        int
            La distance totale du chemin.
        """
        dist_tot=0
        for i in range(len(chemin)-1):
            dist_tot+=self.distances[chemin[i]][chemin[i+1]]
        return dist_tot
    

    def generer_tous_chemins(self):
        """
        Génère tous les chemins possibles en utilisant l'algorithme d'optimisation par colonie de fourmis.
        Retourne
        -------
        list
            Une liste de tuples, où chaque tuple contient un chemin et sa distance totale.
        """
        tous_chemin=[]
        for i in range(self.n_fourmis):
            n=len(self.distances)
            nb_villes=len(self.distances)
            num_ville_dep=random.randint(0,n-1)
            chemin=[num_ville_dep]
            while len(chemin)!=nb_villes: 
                proba=self.calculer_probabilites_mouvement(chemin)
                ville_suivante=self.choisir_ville_suivante(proba)
                chemin.append(ville_suivante)
            dist_tot=self.calculer_distance_chemin(chemin)
            tous_chemin.append([chemin,dist_tot])
        return tous_chemin

    

        

    def calculer_probabilites_mouvement(self, chemin):
        """
        Calcule la probabilité de se déplacer vers chaque ville étant donné le chemin actuel.

        Paramètres
        ----------
        chemin : list
            Une liste d'indices représentant un chemin.

        Retourne
        -------
        list
            Une liste de probabilités, où chaque probabilité est la probabilité de se déplacer vers chaque ville étant donné le chemin actuel.
        """
        
        proba=[]
        for l in range(len(self.distances)):
            if l not in chemin:
                p=(self.pheromones[chemin[-1]][l]**self.alpha)*(1/self.distances[chemin[-1]][l])**self.beta
                proba.append(p)
            else:
                proba.append(0)
        return proba

        



    def choisir_ville_suivante(self, probabilites):
        """
        Choisit la prochaine ville en fonction des probabilités données.

        Paramètres
        ----------
        probabilites : list
            Une liste de probabilités, où chaque probabilité est la probabilité de se déplacer vers chaque ville.

        Retourne
        -------
        int
            L'indice de la ville choisie comme prochaine ville.
        """

        list=[i for i in range(len(probabilites))]
        ville_suivante=random.choices(list,probabilites)[0]
        return ville_suivante


    def deposer_pheromones(self, tous_chemins):
        """
        Dépose des phéromones sur les meilleurs chemins.

        Paramètres
        ----------
        tous_chemins : list
            Une liste de tuples, où chaque tuple contient un chemin et sa distance totale.

        Retourne
        -------
        None
        """
        meilleurs=sorted(tous_chemins, key=lambda x:x[1])
        meilleurs=meilleurs[:self.n_meilleurs]
        for chem,dist in meilleurs:
            for i in range(len(chem)-1):
                self.pheromones[chem[i]][chem[i+1]]+=1/dist

    def evaporer_pheromones(self):
        n=len(self.pheromones)
        for i in range(n):
            for j in range(n):
                self.pheromones[i][j]*=self.decroissance


if __name__ == "__main__":
    distances = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]
    


    # Créer une instance de la colonie de fourmis
    colonie_fourmis = AntColony(distances=distances, n_fourmis=3, n_meilleurs=5, n_iterations=100, decroissance=0.95, alpha=1, beta=2)
    
    def callback_maj(iteration, meilleur_chemin, pheromones):
        """
        Fonction de callback appeler après chaque itération.

        Paramètres
        ----------
        iteration : int
            L'itération actuelle.
        meilleur_chemin : tuple
            Le meilleur chemin trouvé jusqu'à présent.
        pheromones : list
            La matrice des phéromones.

        Retourne
        -------
        None
        """
        if iteration % 10 == 0:
            print(f"Itération {iteration}: Meilleur chemin {meilleur_chemin} avec distance {colonie_fourmis.meilleure_distance}")
            print("Matrice des phéromones:")
            for ligne in pheromones:
                print(ligne)

    # Créer un événement d'arrêt
    evenement_arret = threading.Event()
    # Exécuter l'algorithme dans le thread principal pour cet exemple
    colonie_fourmis.run(callback_maj, evenement_arret)
    # Meillere chemin trouvé
    print(f"Meilleur chemin trouvé : {colonie_fourmis.meilleur_chemin} avec une distance de {colonie_fourmis.meilleure_distance}")