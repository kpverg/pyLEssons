d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2={
    7:"lucky seven",
    10:"ten",
    3:"new three",
}
#update method
d.update(d2)
for key, value in d.items():
    print(key,value)
print("*"*20)
d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key,value)

#keys
# #newDict=dict.fromkeys(pantry_items)
# newDict=dict.fromkeys(pantry_items,0) #create a new dict with keys from the given ,0 give the 0 to values
# print(newDict)


# keys=d.keys()
# print(keys)
# for item in keys:
#     print(item)
#values

v=d.values()
print(v)
d[11]="eleven"
print(v)
print( "eleven" in v)