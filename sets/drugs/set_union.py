# farmAnimals={"sheep","hen","horse","goat"}
# wildAnimals={"lion","elephant","tiger","goat","panther","horse"}

# allanimals=farmAnimals.union(wildAnimals)
# allanimals2=farmAnimals|wildAnimals
# print(allanimals)
# print(allanimals2)

from perscriptionData import adverse_interactions
medsToWatch=set()

for interaction in adverse_interactions:
    medsToWatch=medsToWatch.union(interaction)
    medsToWatch=medsToWatch|interaction
    medsToWatch.update(interaction) #  |=
    medsToWatch|=interaction
medsToWatch.update(*adverse_interactions)
print(sorted(medsToWatch))
print()
print(*sorted(medsToWatch),sep='\n')