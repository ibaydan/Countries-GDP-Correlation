#!/bin/python3

import csv
import pandas as pd                                                                                                                                                                                                              
import numpy as np                                                                                                                                                                                                               
from collections import Counter                                                                                                                                                                                                  
                                                                                                                                                                                                                                 
#list that contains subsaharan codes                                                                                                                                                                                             
SubSaharanCodes=list()                                                                                                                                                                                                           
                                                                                                                                                                                                                                 
#List that Contains subsaharan rows                                                                                                                                                                                              
SubSaharanList= list()                                                                                                                                                                                                           
                                                                                                                                                                                                                                 
#List that containes correlated Countries                                                                                                                                                                                        
CorrelationList=list()                                                                                                                                                                                                           
                                                                                                                                                                                                                                 
#Convert string to float , NaN                                                                                                                                                                                                   
def convertToInteger(mylist):                                                                                                                                                                                                    
    newlist=list()                                                                                                                                                                                                               
    #Copy Strings to new list                                                                                                                                                                                                    
    newlist.extend(mylist[:3])                                                                                                                                                                                                   
    #convert numerical strings to new list by converting float                                                                                                                                                                   
    for element in mylist[4:]:                                                                                                                                                                                                   
        if(element == ''):                                                                                                                                                                                                       
            newlist.append(np.nan)                                                                                                                                                                                               
        else:                                                                                                                                                                                                                    
            newlist.append(float(element))                                                                                                                                                                                       
    #Return manupilated new list                                                                                                                                                                                                 
    return newlist                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                              
#OpenMetadata file and get SubSaharan Country codes                                                                                                                                                                                                                           
with open('Metadata_Country.csv', newline='') as csvfile:                                                                                                                                                                                                                     
    #Read csv                                                                                                                                                                                                                                                                 
    CodeReader = csv.reader(csvfile, delimiter=',', quotechar='"')                                                                                                                                                                                                            
    for row in CodeReader:                                                                                                                                                                                                                                                    
        #Select SubSaharan Country                                                                                                                                                                                                                                            
        if (row[2] == "Sub-Saharan Africa"):                                                                                                                                                                                                                                  
            #Add to list                                                                                                                                                                                                                                                      
            SubSaharanCodes.append(row[1])                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                              
print("SubSaharan Codes")                                                                                                                                                                                                                                                     
print(SubSaharanCodes)                                                                                                                                                                                                                                                        

#Read GDP file and add Sub saharan countries to the SubSaharanList
with open('GDP.csv', newline='') as csvfile:
    #Read csv
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')    
    for row in spamreader:
        #print(row)
        #Select SubSaharan Country
        if(row[1] in SubSaharanCodes):
            #Add to list
            SubSaharanList.append(convertToInteger(row))
            
#Get one SubSaharan country
for C1 in SubSaharanList:
    #Convert anual gdps to dataframe 
    dfC1 = pd.DataFrame(C1[4:])
    #Set highest correlation value for this round
    HighestValue=0
    #Set Country value for this round
    HighestC=''
    #Remove 1. country from list
    SubSaharanListVar=list(SubSaharanList)
    SubSaharanListVar.remove(C1)
    #Get new country
    for C2 in SubSaharanListVar:
        #Convert anual gdps to dataframe
        dfC2 = pd.DataFrame(C2[4:])
        #Correlate with C1
        val=dfC1.corrwith(dfC2).values
        #If C2 is lower than
        if(HighestValue > val):
            pass
        #If C2 is higher than
        else:
            #Update highest value and country
            HighestValue=val
            HighestC=C2[1]
    print(C1[1]+" "+HighestC)
    #Add best correlation C1 and C2 to the list 
    CorrelationList.append(C1[1])
    CorrelationList.append(HighestC)
    
#Show most best correlated country
print(Counter(CorrelationList))

C=Counter(CorrelationList)

MostUsedCountryCode=max(C, key=C.get)

for Country in SubSaharanList:
    if MostUsedCountryCode == Country[1]:
        print("\n\n")
        print ("Best correlated country is ", Country[0]) 
        print("\n\n")
        break