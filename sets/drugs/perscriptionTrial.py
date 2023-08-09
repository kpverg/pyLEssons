from perscriptionData import *
patientsTrial=[
    "Anne",
    "Bob",
    "Charley",
    "Denise",
    "Eddie"
]
for patient in patientsTrial:
    prescription=patients[patient] 
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except:
        print(f"patient {patient} does not taking warfarine.")
    
    print(patient,prescription) 