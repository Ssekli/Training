# création de table de multiplication
def table(n, min, max):
    if min>max :
        print("erreur")
        return

    else :
        for i in range(min, max+1) :
            calcul = n * i
            print(f"{n}*{i}={calcul}")

table(5, 1, 12)