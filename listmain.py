names = []

while True :
    name = input("Quel est le nom ?)")
    if name == "":
        break
    names.append(name)

print(names)
names.sort() #triage alphabet A > Z > a > z
print(names)