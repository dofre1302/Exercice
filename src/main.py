import time

import compte
users_listcc = []

fred = compte.CompteCourant("Fred")
users_listcc.append(fred)

linda = compte.CompteCourant("Linda")
users_listcc.append(linda)

yvan = compte.CompteCourant("Yvan")
users_listcc.append(yvan)

def login():
    nom_utilisateur = input("Bienvenue à la sociéte Géniale\nEntrez votre nom d'utilisateur : ")
    for user in users_listcc:
        if user.nom_utilisateur == nom_utilisateur:
            return user
    raise ValueError("nom d'utilisateur inconnu")

def versement():
    versement = float(input("Entrez le montant du versement: "))
    user_login.versement(versement)
    return("Votre nouveau solde est de {} €".format(user_login.solde))

def retrait():
    retrait = float(input("Entrez le montant du retrait:"))
    user_login.retrait(retrait)
    return("Votre nouveau solde est de {} €".format(user_login.solde))

user_login = login()

def choix():
    choix = input("choisissez une opération,\nPour effectuer un retrait tapez 1\nPour effectuer un versement tapez 2\n: ")
    if choix =="1":
        return retrait()
    elif choix =="2":
        return versement()
    else:
        raise ValueError("opération invalide")

def accueil():
    print("Ravi de vous revoir {},\nCompte : n° {},\nSolde du Compte : {} €" .format(user_login.nom_utilisateur, user_login.numero_compte, user_login.solde))
    return

print(accueil())

while True:
    print(choix())





