#algo valeur la plus petite


driver_name = ["Bob", "Brian", "Paul", "Jake", "Mary", "Car", "Max"]
driver_distance = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

min_index = 0
min_distance = driver_distance[0]
for i in range(len(driver_distance)) :
    distance = driver_distance[i]
    if distance < min_distance :
        min_distance = distance
        min_index = i


print(f"Distance minimale : {min_distance} km")
print(f"Index de la distance minimale : {min_index}")
print(f"Le chauffeur s'appelle {driver_name[min_index]}")

#driver_distance.sort() trie mais casse l'index
 

#Meilleur facon car liste peu contenir liste ou tupple 
name_distances = [("Bob", 1.5), ("Brian", 2.2), ("Paul", 0.4), ]

min_distance_name = name_distances[0]
for name_distance in name_distances :
    if name_distance[1] < min_distance_name [1] :
        min_distance_name = name_distance

print(f"Distance minimale {min_distance_name[1]} Nom du pilote : {min_distance_name[0]}")