import csv
import itertools
import numpy

def remoteWrongData (dataInput):    #řadit pod sebe bez čárek
    for row in dataInput:  
        x = []
        try:
            #writer.writerow([float(row[5])])
            all.append([float(row[5])])
        except ValueError:
            pass   
 
def averageSevenData (dataInput):
    steps = 3
    print(len(dataInput))
    
def choiceSevenData (dataInput):
    seventhLine = itertools.islice(dataInput, 0, None, 7)   #součást itertools
    for row in seventhLine:    
        writer.writerow([row[0],row[1],row[3],row[4]])     
            
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput,\
     open("result.csv","w", encoding="utf8") as vysledek1:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    writer = csv.writer(vysledek1)
    all = []
    for row in dataInput:  
        all.append(row[5])
    print(all)
    """
    seventhLine = itertools.islice(dataInput, 0, None, 7)   #součást itertools
    for row in seventhLine:    
        writer.writerow([row[0], row[1], row[2], row[3], row[4]])
        """
    
    
    