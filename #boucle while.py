#boucle et fonctions
# bug de type dans fonction print

def demander_age() :
    age_int = 0
    while age_int == 0 :
        age_str = input("Quel est votre age ?")
        try:
            age_int = int(age_str)
        except ValueError:
            print("erreur entrez un nombre")
    return age_int



def demander_nom() :
    reponse_nom = ""
    while reponse_nom == "" :
        reponse_nom = input("Quel est votre nom ?")
    return


nom = demander_nom()

age = demander_age()

print("vous vous appelez" + nom + ",vous avez" + str(age) + "ans")
print("L'an prochain vous aurez" + str(age+1) + "ans")
