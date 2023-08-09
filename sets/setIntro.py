# union  connection of two sets
# farmAnimals.union(wildAnimals)


# intersection common elements
# farmAnimals.intersection(wildAnimals)

#subtracked  any items from wildAnimals are removed from farmAnimals 
# farmAnimals.difference(wildAnimals)
# symetric difference the opposite of intersection
# farmAnimals.symmetric_difference(wildAnimals)
# 
farmAnimals={'cow','sheep','hen','goat','horse'}
print(farmAnimals)
for animal in farmAnimals:
    print(animal) # u cant index and you cant slice a set
    
moreAnimals={'goat','hen','cow','sheep','horse'}
if moreAnimals== farmAnimals:
    print("sets are equal")
else:
    print("sets are deferent")
    
    
numbers=set(range(0,20,2))
print(numbers)