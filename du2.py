import csv
import itertools
import numpy

def remoteWrongData (dataInput):    #řadit pod sebe bez čárek
    for row in dataInput:  
        try:
            writer.writerow([row[0],row[1],row[2],row[3],row[4],float(row[5])])
        except ValueError:
            pass   

#def choiceFifthColumn (dataInput): #zde bude vstup z remoteWrongData

#def averageSevenData (dataInput): #zde bude vstup z choice FifthColumn
    
def choiceSevenData (dataInput): #zde bude vstup z remoteWrongData
    seventhLine = itertools.islice(dataInput, 0, None, 7)   #součást itertools
    for row in seventhLine:    
        writer.writerow([row[0],row[1],row[3],row[4]])     

#def mergeWeekData (dataInput): #spojit choiceSevenData a averageSevenData
            
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput,\
     open("result.csv","w", encoding="utf8") as vysledek1:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    writer = csv.writer(vysledek1)