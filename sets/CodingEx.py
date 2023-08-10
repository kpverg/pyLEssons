text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

 
lstWords=list(text.split())
setlst=set(lstWords)
preps_used=setlst.intersection(prepositions)
print(preps_used)