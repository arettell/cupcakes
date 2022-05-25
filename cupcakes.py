one_cupcake = int()
cupcakes = [0, 0, 0, 0, 0]
cupcake_average = float()
total_cupcakes = int()
one_type = str()
highest_value = int()
highest_index = int()



cupcakes = [10, 6, 7, 8, 5]
types = ['Red velvet', 'Vanilla', 'Chocolate', 'Strawberry', 'Lemon']

print("Cupcake Type\tNumber Sold")
print("*" * 27)

#printing our cupcakes list
for index in range(0, len(cupcakes)):
    one_cupcake = cupcakes[index]
    one_type = types[index]
    print(one_type, "\t", one_cupcake)
#end for

#determine the average amount of cupcakes sold
for index in range(0, len(cupcakes)):
    one_cupcake = cupcakes[index]
    total_cupcakes = total_cupcakes + one_cupcake
#end for

cupcake_average = total_cupcakes/len(cupcakes)
print()
print("Average cupcakes sold: ", format(cupcake_average, '.2f'))
print()


#initializing highest  value
highest_value = cupcakes[0]
#for finding highest value
for index in range(0, len(cupcakes)):
    one_cupcake = cupcakes[index]
    if one_cupcake > highest_value:
        highest_value = one_cupcake
        highest_index = index


print("the cupcake that sold the highest number: ", types [highest_index])
print("Highest number of cupcakes sold: ", cupcakes[highest_index])
