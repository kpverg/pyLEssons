data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

filename = '/home/thedoctor/Documents/pyLEssons/files/floweers/plants_write.txt'

with open(filename,'w') as plants:
   for plant in data:
       plants.write(plant)
 
filename = '/home/thedoctor/Documents/pyLEssons/files/floweers/testnumbers.txt'
with open(filename,'w') as test:
    for i in range(10):
        #print(i, file=test)
        test.write(str(i)+'\n')