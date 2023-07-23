from contents import pantry,recipes

display_dict={}
for index,key in enumerate(recipes):

    #print(index, key,recipes[key])
    #print(index, key)
    display_dict[str(index+1)]=key

while True:
    print(f"please chose a recipe")
    print("-"*20)
    
    for key,value in display_dict.items():
        print(f"{key} : {value}")
    choice=input(":> ") 
    if choice=="0":
        break
    elif choice in display_dict:
        selectedItem=display_dict[choice]
        print(f"you have selected {selectedItem}")
        print(f"Checking ingrediants...")
        ingredients=recipes[selectedItem]
        print(ingredients)
        for food_item,requiredQuantity in ingredients.items():
            quantityInPantry=pantry.get(food_item,0) #to mhden mpainei gia thn periptwsh pou den brethei           
            if requiredQuantity>quantityInPantry:
                quantityToBuy=requiredQuantity-quantityInPantry
                print(f"\tYou need to buy {quantityToBuy} of {food_item} ")    
            else:
                print(f"\tYou have the nessesary quanity of {food_item}")