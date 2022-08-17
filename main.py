#boucle et fonctions

def demander_nom() :
    nom = ""
    while nom == "" :
        nom = input("Quel est votre nom ?")
    return nom


def demander_age(nom) :
    age_int = 0
    while age_int == 0 :
        age_str = input(nom + "Quel est votre age ?")
        try:
            age_int = int(age_str)
        except ValueError:
            print("erreur entrez un nombre")
    return age_int

def afficher_information_personne(nom, age) :
    print()
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans.")
    print()
    if age >= 18: 
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
        

nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personne(nom1, age1)
afficher_information_personne(nom2, age2)


