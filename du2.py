import csv
import itertools
import numpy
  
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput,\
     open("result1.csv","w", encoding="utf8") as vysledek1:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    writerWeek = csv.writer(vysledek1)   
    rowNumber = -1
    avSevenDay = 0
    for row in dataInput:
        rowNumber += 1
        if rowNumber%7 == 0:
            firstDayWeek = row
        rowNumberOneBig = rowNumber + 1
        avSevenDay += float(row[5])/7
        if rowNumberOneBig%7 ==0:
            firstDayWeek[5] = float(avSevenDay)
            print(firstDayWeek)
            avSevenDay = 0
            

    

"""
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    rowsmax = max(dataInput, key=lambda row: float(row[5]))
    print(rowsmax)
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    rowsmin = min(dataInput, key=lambda row: float(row[5]))
    print(rowsmin)
"""