import csv
  
with open ("Data_zelivka.csv", encoding="utf8") as csvInput,\
     open("vystup_7dni.csv","w", encoding="utf8") as csvOutput:
    dataInput = csv.reader(csvInput, delimiter = ",")
    writerWeek = csv.writer(csvOutput)   
    writerYear = csv.writer(csvOutput)  
    rowNumber = 0
    avSevenDay = 0
    for row in dataInput:     
        if rowNumber % 7 == 0:
            firstDayWeek = row
        try:
            avSevenDay += float(row[5])/7
        except ValueError:
            print("Na řádku ",dataInput.line_num ," je chybně zadaná hodnota, a proto ji program nezapočítá")
        except:
            print("Na řádku ",dataInput.line_num ," je nesprávně dlouhé pole a proto ji program nezapočítá")
        print(dataInput.line_num)
        if (rowNumber % 7 == 6):
            firstDayWeek[5] = avSevenDay
            writerWeek.writerow(firstDayWeek)
            avSevenDay -= avSevenDay
        rowNumber += 1
        
            

    

"""
with open ("Data_zelivka.csv", encoding="utf8") as csvInput:
    dataInput = csv.reader(csvInput, delimiter = ",")
    for row in dataInput:
        par = row
        try:
            par[5] = float(row[5])
        except:
            pass
        
    rowsmax = max(dataInput, key=lambda row: par[5])
    print(rowsmax)
    """

"""
with open ("Data_zelivka.csv", encoding="utf8") as csvInput:
    dataInput = csv.reader(csvInput, delimiter = ",")
    rowsmin = min(dataInput, key=lambda row: row[5])
    print(rowsmin)
    """
    
