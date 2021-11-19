import csv
import itertools
import numpy

            
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput,\
     open("result.csv","w", encoding="utf8") as vysledek1:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    writer = csv.writer(vysledek1)
    numRow = -1
    for row in dataInput:
        numRow = numRow + 1
        choiceSevenDay = numRow % 7
        if choiceSevenDay == 0:
            try:
                print(row[0],row[1],row[2],row[3],row[4],float(row[5]))
            except ValueError:
                pass


            