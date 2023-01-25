import uuid
from abc import ABC


class Compte(ABC):
    """
        Abstract class Compte
    """
    def __init__(self, nom_utilisateur: str, numero_compte: int = uuid.uuid4(), solde: int = 0) :
        self.solde = solde
        self.numero_compte = numero_compte
        self.nom_utilisateur = nom_utilisateur


    def versement(self):
        pass

    def retrait(self):
        pass

    def __str__(self) ->str:
        """
        retourne le solde du compte
        """
        return "CompteCourant - Solde : {}".format(self.solde)

    def __repr__(self):
        pass

class CompteCourant(Compte):
    def __init__(self, nom_utilisateur, autorisation_decouvert: int = -100, pourcentage_agios: float = 1.1):
        super().__init__(nom_utilisateur)
        self.decouvert = autorisation_decouvert
        self.agios = pourcentage_agios

    def versement(self, versement):
            if versement <= 0:
                raise ValueError ("Le montant doit être supérieur à 0.")
            self.solde += versement

    def retrait(self, retrait):
            self.solde -= retrait
            if retrait <= 0:
                raise ValueError ("le montant doit être supérieur à 0")
            if retrait > (self.solde - self.decouvert):
                raise ValueError("Opération impossible, vous avez atteint votre limite de découvert.")
            if self.solde < 0:
                self.solde *= self.agios




class CompteEpargne(CompteCourant):
    def __init__(self, nom_utilisateur, pourcentage_interet: float = 1.0):
        super().__init__(nom_utilisateur)
        self.interet = pourcentage_interet
