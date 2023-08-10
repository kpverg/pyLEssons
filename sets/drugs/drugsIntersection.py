import perscriptionData

for patient in perscriptionData.patients:
    for combo in perscriptionData.adverse_interactions:
        if len(perscriptionData.patients[patient].intersection(combo))>=2:
            print(f" o  {patient} exei probhma sto sundiasmo farmakwn {combo}")
        #print(len(perscriptionData.patients[patient].intersection(combo)))
    print()
    #perscriptionData.patients[patient].intersection(perscriptionData.adverse_interactions)
    