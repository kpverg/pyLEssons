from  contents import pantry
chicken_quantity=pantry.setdefault("chicken",0)
print(f"chicken quantity : {chicken_quantity}" )


beans_quantity=pantry.setdefault("beans",0)      #to set defaylt eisagei neo stoixeio sthn pantry h opou xrhsimopoihthei
print(f"beans quantity : {beans_quantity}" )

ketchup_quantity=pantry.get("ketchup",0)
print(f"ketcup quantity : {ketchup_quantity}" )

for key, value in sorted(pantry.items()):
    print(key,value)