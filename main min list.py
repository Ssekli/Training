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