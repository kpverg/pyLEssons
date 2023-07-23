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

def show_me():
    for key,value in vehicles.items():
        print(key , vehicles[key],sep=', ',end=".\n")
    print()

vehicles['startfighter']='Lockheed F-104'
vehicles['learjet']='Bombardier Learjet 75'
vehicles['toy']='glider'

#for key,value in vehicles.items():
#   print(key , vehicles[key],sep=', ',end=".\n")
#print()

#Upgrade A value of a Dict
vehicles['virago']='Yamaha XV535'
show_me()


#DEleting Items FRom DICTIONARY
del vehicles['can-am']
vehicles.pop('f1',None)  #ean den to vrei krasarei, opote to vazw ,None.An den iparxei gurnaei to None
#an to brei gurnaei to value oxi to none
#vehicles.pop('f1',"Returning Data When key cant be found")
show_me()
