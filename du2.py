import csv
import itertools
import numpy


            
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput,\
     open("result1.csv","w", encoding="utf8") as vysledek1:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    writer = csv.writer(vysledek1)   
    numRow = 0
    aveSevenDay = 0
    for row in dataInput:
        numRow = numRow + 1
        print(numRow)
        choiceSevenDay = numRow % 7
        try:
            aveSevenDay += float(row[-1])
        except ValueError:
            pass
        if choiceSevenDay == 0:
            aveSevenDay = aveSevenDay/7
            writer.writerow([row[0],row[1],row[2],row[3],row[4],float(aveSevenDay)])
    """
    minTemp = [] 
    maxTemp = [] 
    for row in dataInput:
        try:
            minTemp.append([row[2],row[3],row[4],float(row[5])])
            maxTemp.append([row[2],row[3],row[4],float(row[5])])
        except:
            pass
    theindexmin=minTemp.index(min(minTemp))
    theindexmax=maxTemp.index(max(maxTemp))
    print("Minimální hodnota: \n", minTemp[theindexmin]) 
    print("\n\nMaximální hodnota: \n",maxTemp[theindexmax]) 
        """