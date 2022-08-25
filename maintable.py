# création de table de multiplication
def table(n, min=1, max=10):
    if min>max :
        print("erreur")
        return

    for i in range(min, max+1) :
        calcul = n * i
        print(f"{n}x{i}={calcul}")

table(5, 1, 12)
