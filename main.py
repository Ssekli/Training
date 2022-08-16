nom_de_la_personne = input("Quel est ton nom ?")
age = input("Quel est ton age ?")


try :
    age_prochain = int(age) + 1

    
except : ValueError
    print("entrez un nombre")


else :
    print("je m'appelle" + nom_de_la_personne + "et j'ai" + age +"ans")
    print("L'an prochain, vous aurez " + age_prochain + ".")