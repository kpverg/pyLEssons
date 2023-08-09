available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }


current_choise=None
computer_parts={}
while current_choise !="0":
    if current_choise in available_parts:
        chosenPart=available_parts[current_choise]
        if current_choise in computer_parts:
            #to exw kai to svinw           
            print(f"Removing {chosenPart}")
            computer_parts.pop(current_choise)
        else:
            #den to exw kai to  bgazw
            print(f"Adding {chosenPart}")
            computer_parts[current_choise]=available_parts[current_choise]
        print(f"your selection contains {computer_parts}")
    else:
        print("Select an Option From List")
        for key,value in available_parts.items():
            print(f"{key}:{value}")
        print(f"0:to finish")
    current_choise=input(">")