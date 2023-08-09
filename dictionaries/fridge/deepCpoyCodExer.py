from contents import recipes
import copy


def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.
 
    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.
 
    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """
    new_dict = {}
    #new_dict=copy.deepcopy(d) #1 solution
    for key, value in d.items():
        
        new_dict[key]=value.copy()
    # keys=list(d.keys())
    # values=list(v)
    
    #v=d.values()
    
    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])