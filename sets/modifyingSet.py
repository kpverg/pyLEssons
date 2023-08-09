# numbers={*""}
numbers=set()
numbers.add(1)
print(numbers ,type(numbers))
LooppSet=set()
# while len(LooppSet)<4:
#     nextInt= int(input("Please Give me an integer"))
#     LooppSet.add(nextInt)
# print(LooppSet)

#remove duplicates

colors=["blue","blue","blue","blue","blue","red","red","red","red","red","yellow","yellow","yellow","yellow","yellow","green","green","green","green","green"]
# uniqueColors=set()
# for color in colors:
#     uniqueColors.add(color)
uniqueColors=set(colors)
uniqueColorsSortedCreatesAList=sorted(set(colors))
#create a list with unique colors ,keeping the order they appeared

unColor=list(dict.fromkeys((colors)))
print(uniqueColors)
print(uniqueColorsSortedCreatesAList)

print(unColor)