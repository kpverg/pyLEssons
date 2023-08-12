filename = '/home/thedoctor/Documents/pyLEssons/files/countrisParsing/country_info.txt'
Countries_info={}
with open(filename) as CountriesFile:
    CountriesFile.readline() # diavazei tin prwth eggrfi, diladi tin epikefalida opote...
    for row in CountriesFile:  #apo edw kai pera diabazei to epomeno keimeno(oxi thn prwth grammh)
        data=row.strip('\n').split('|')
        country, Capital,code, code3, dialing, TimeZone, Currency=data
        country_info={
             'name':country,
             'Capital':Capital,
             'code':code, 
             'code3':code3, 
             'dialing':dialing, 
             'TimeZone':TimeZone, 
             'Currency':Currency,            
         }
        #print(country_info)
        Countries_info[country.casefold()] = country_info
        Countries_info[code.casefold()] = country_info
    # 
    
while True:
    UsrInput=input("Please Give Me a Counttry ")
    if UsrInput in Countries_info:
        countryData=Countries_info[UsrInput]
        print(countryData['name'])
        print(f"The capital of the country {countryData['name']},{countryData['code'].upper()} : {countryData['Capital']}" )          
    elif UsrInput=="quit":
        break
    else:
        print("Not found")
        continue
    
       