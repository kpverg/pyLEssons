from contents import pantry,recipes
def addItemsToShoppingList( data:dict,item:str,amount:int)-> None:
    # if  item in data:    ###multiple lines comment:  select text  cntl+/
    #     data[item]+=amount    
    # else:
    #     data[item]=amount

#setdafault
    data[item]=data.setdefault(item,0)+ amount  #an to brei, auksanei to ammount, an den to brei, kanei nea eggrafi me amount 0



display_dict={}
for index,key in enumerate(recipes):

    #print(index, key,recipes[key])
    #print(index, key)
    display_dict[str(index+1)]=key
    shopingList={}
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
                addItemsToShoppingList(shopingList,food_item,quantityToBuy)  #eisagwgi se lista stoixeiwn me function
            else:
                print(f"\tYou have the nessesary quanity of {food_item}")
for things in shopingList.items():  #for things,quantity in shopingList.items():
    print(things)  