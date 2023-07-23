 
totseconds=37000
hours=totseconds//3600

ipoloipo=totseconds%3600

minutes=ipoloipo//60
seconds=ipoloipo%60

print("ta {} analoiontai se {} wres,{} lepta,{} deuterolepta".format(totseconds,hours,minutes,seconds))