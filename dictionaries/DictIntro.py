vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car=vehicles['fiesta']
print(my_car)
commuter=vehicles['virago']
print(commuter)

learner=vehicles.get('jimny')  # .get method
print(learner)



for key in vehicles:
    print(key , vehicles[key],sep=', ',end=".\n")
print()

for key,value in vehicles.items():
    print(key , vehicles[key],sep=', ',end=".\n")
print()