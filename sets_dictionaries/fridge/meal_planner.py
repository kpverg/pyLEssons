from contents import pantry,recipes

display_dict={}
for index,key in enumerate(recipes):

    #print(index, key,recipes[key])
    #print(index, key)
    display_dict[str(index+1)]=key
print(display_dict)