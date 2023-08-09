import copy
animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}
#shallow copy
things=animals.copy() #dimiourgei neo dict(antigrafO)
#things=animals anafaretai sto idio dict

#deepcpoy


print(things)
print("*"*30)
animals["teddy"]="toy"
print(things["teddy"])


animals2 = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

print("*"*30)
things=copy.deepcopy(animals2)
print(things["teddy"])
print(animals2["teddy"])
things["teddy"].append("kiout")
print(id(things["teddy"]),things["teddy"])
print(id(animals2["teddy"]), animals2["teddy"])