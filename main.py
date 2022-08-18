#Fiche personne



def demander_nom() :
    nom = ""
    while nom == "" :
        nom = input("Quel est votre nom ?")
    return nom


def demander_age(nom) :
    age_int = 0
    while age_int == 0 :
        age_str = input(nom + " Quel est votre age ?")
        try:
            age_int = int(age_str)
        except ValueError:
            print("erreur entrez un nombre")
    return age_int

def demander_taille(nom) :
    taille_float = 0.0
    while  taille_float == 0.0 :
        taille_str = input(nom + " Quel est votre taille ?")
        try:
            taille_float = float(taille_str)
        except ValueError:
            print("Entrez un nombre au format 0.00")
    return taille_float
        

def afficher_information_personne(nom, age, taille) :
    print()
    print("vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    print("L'an prochain vous aurez " + str(age+1) + " ans.")
    print()
    if age > 60:
        print("Vous êtes sénior")
    elif age == 17: 
        print("Vous êtes presque majeur")
    elif age >= 12 and age < 18:
        print("Vous êtes adolescent")
    elif age == 18:
        print("Tout juste majeur, félicitation !")
    elif age > 18:
        print("Vous êtes majeur")
    elif age == 1 or age == 2:
        print("Vous êtes bébé")
    elif age < 10:
        print("Vous êtes un enfant")
    else:
        print ("Vous êtes mineur")
   

    print("Votre taille est " + str(taille) + " m")


#nom1 = demander_nom()
#nom2 = demander_nom()

#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

#afficher_information_personne(nom1, age1)
#afficher_information_personne(nom2, age2)

NB_DE_PERSONNES = 3
for i in range(0, NB_DE_PERSONNES):
    nom = demander_nom()
    age = demander_age(nom)
    taille = demander_taille(nom)
    afficher_information_personne(nom, age, taille)
