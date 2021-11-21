import csv

#NAČTENÍ DAT A ZÁKLADNÍ OPERACE  
with open ("Data_zelivka.csv", encoding="utf8") as csvInput,\
     open("vystup_7dni.csv","w", encoding="utf8") as csvOutputWeek,\
     open("vystup_rok.csv","w", encoding="utf8") as csvOutputYear:
    dataInput = csv.reader(csvInput, delimiter = ",")
    writerWeek = csv.writer(csvOutputWeek)   
    writerYear = csv.writer(csvOutputYear)  
    
    #DEFINICE POMOCKÝCH PROMĚNNÝCH 
    rowNumber = 0
    avSevenDay = 0
    residueDay = 0
    residueYear = 0
    dayYear = 0
    avYear = 0
    
    #CYKLUS ČTOUCÍ ŘÁDKY VSTUPU
    for row in dataInput:     
        if rowNumber % 7 == 0:
            firstDayWeek = row           
        try:
            avSevenDay += float(row[5])
            residueDay += 1
            avYear += float(row[5])
            residueYear += 1 
        except ValueError:
            print("Na řádku ",dataInput.line_num ," je chybně zadaná hodnota, a proto ji program nezapočítá")
        except:
            print("Na řádku ",dataInput.line_num ," je nesprávně dlouhé pole a proto ji program nezapočítá")

        if dataInput.line_num == 1:
            firstDayYear = row
            calculateYear = int(firstDayYear[2])
        theYear = int(row[2])
        if theYear != calculateYear:
            avYear /= dayYear
            avYear = "{:.4f}".format(avYear)
            firstDayYear[5] = avYear
            writerYear.writerow(firstDayYear)
            avYear = float(avYear)
            avYear -= avYear
            dayYear -= avYear 
            residueYear -= residueYear
            firstDayYear = row
            calculateYear = int(firstDayYear[2])
        dayYear += 1
        #ZÁPIS DO SOUBORU S TÝDENNÍMI SOUBORY
        if (rowNumber % 7 == 6):
            avSevenDay /= 7
            avSevenDay = "{:.4f}".format(avSevenDay)
            firstDayWeek[5] = avSevenDay
            writerWeek.writerow(firstDayWeek)
            residueDay -= residueDay
            avSevenDay = float(avSevenDay)
            avSevenDay -= avSevenDay    #odstranění řádku
        rowNumber += 1

    if (calculateYear == theYear):
        avYear /= dayYear
        avYear = "{:.4f}".format(avYear)
        firstDayYear[5] = avYear
        writerYear.writerow(firstDayYear)


    #PŘIDÁNÍ POSLEDNÍ ŘÁDKU SE SEDMIDENNÍM PRŮMĚREM
    if (rowNumber % 7 != 6):    
        avSevenDay /= residueDay
        avSevenDay = "{:.4f}".format(avSevenDay)
        firstDayWeek[5] = avSevenDay
        writerWeek.writerow(firstDayWeek)

    


"""        
with open ("Data_zelivka.csv", encoding="utf8") as csvInput:
    dataInput = csv.reader(csvInput, delimiter = ",")
    rowsmax = max(dataInput, key=lambda row: row[5])
    print(rowsmax)

with open ("Data_zelivka.csv", encoding="utf8") as csvInput:
    dataInput = csv.reader(csvInput, delimiter = ",")
    rowsmin = min(dataInput, key=lambda row: row[5])
    print(rowsmin)
    """

    
