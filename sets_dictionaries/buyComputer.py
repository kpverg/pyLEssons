available_parts = {"1": "computer",
                       "2": "monitor",
                       "3": "keyboard",
                       "4": "mouse",
                       "5": "hdmi cable",
                       "6": "dvd drive",
                       }
current_choise=None
computer_parts=[]
while current_choise !="0":
    if current_choise in available_parts:
        chosenPart=available_parts[current_choise]
        if chosenPart in computer_parts:
            #uparxei opote to svinw
            computer_parts.remove(chosenPart)
            print(f"Removing {chosenPart}")            
            print(f"Your selection has {computer_parts}")
        else:
            #den iparxei opote to vazw
            computer_parts.append(chosenPart)
            print(f"Adding {chosenPart}")  
            print(f"Your selection has {computer_parts}")
    else:
        print("Select an Option From List")
        for key,value in available_parts.items():
            print(f"{key}:{value}")
        print(f"0:to finish")
    current_choise=input(">")   