#bird <= animals suset
#animals >=birds supersets
# bird< animals bird are subset of animal and have less items on it
#animal>birds animal is a superset of bird and have more ites on it
#
animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}
guarden_birds = {'Robin', 'Swallow', 'Wren'}
print(birds.issubset(animals))
print(animals.issuperset(birds))
print(birds<=animals)
print(birds<animals)
print(birds==guarden_birds)
print(birds<= guarden_birds) #subset
print(birds< guarden_birds) #proper subset

print("*"*80)
required_skills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}
succeded= set()
for ipospsifios ,prosonta in candidates.items():
    #if prosonta.issuperset(required_skills):
    if prosonta> set(required_skills):#proper superset
        succeded.add(ipospsifios)    
        
print(succeded)