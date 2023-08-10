from perscriptionData import patients
patientsTrial={"Anne","Bob","Charley", "Denise","Eddie"}

while patientsTrial:
    patient=patientsTrial.pop()  #kanei pop ena tuxaio element apo to set kai to afairei
    perscrption=patients[patient]
    print(f"{patient}: {perscrption}")

