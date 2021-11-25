import csv
from typing import IO

#NAČTENÍ DAT A ZÁKLADNÍ OPERACE  

try:
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
            if rowNumber % 7 == 0: #výběr pondělí
                firstDayWeek = row     
            if dataInput.line_num == 1: #výběr prvního dne roku
                firstDayYear = row
                calculateYear = int(firstDayYear[2])  #pouze úprava na int
            theYear = int(row[2]) #zápis druhého sloupce do roku (bez int)
            try:
                avSevenDay += float(row[5]) #suma dní v týdnu
                residueDay += 1 
                avYear += float(row[5]) #suma dní v týdnu
                residueYear += 1 
            except ValueError:
                print("Na řádku ",dataInput.line_num ," je chybně zadaná hodnota, a proto nedisponuje ve výpočtu průměrů") #výjimka neodstraní celý řádek (neustále existence při opakování 7 dní)
            except IndexError:
                print("Na řádku ",dataInput.line_num ," je nesprávně dlouhé pole, a proto nedisponuje ve výpočtu průměrů") #výjimka neodstraní celý řádek (neustále existence při opakování 7 dní)
            #ZÁPIS DO SOUBORU S ROČNÍMI HODNOTAMI
            if theYear != calculateYear:
                avYear /= dayYear #průměr za rok
                avYear = "{:.4f}".format(avYear)
                firstDayYear[5] = avYear 
                writerYear.writerow(firstDayYear) #zápis do souboru
                avYear = float(avYear)
                firstDayYear = row
                calculateYear = int(firstDayYear[2])
                avYear = 0 #vynulování před znovu-projetím cyklu
                residueYear = 0 #vynulování před znovu-projetím cyklu
            dayYear += 1
            
            #ZÁPIS DO SOUBORU SE SEDMIDENNÍMI HODNOTAMI
            if (rowNumber % 7 == 6):
                avSevenDay /= 7
                avSevenDay = "{:.4f}".format(avSevenDay) #formátování a zároveň převod na string
                firstDayWeek[5] = avSevenDay
                writerWeek.writerow(firstDayWeek)
                residueDay = 0
                avSevenDay = float(avSevenDay)
                avSevenDay = 0    #vynulování před znovu-projetím cyklu
            rowNumber += 1

        #PŘIDÁNÍ POSLEDNÍHO ŘÁDKU S ROČNÍM PRŮMĚREM
        if (calculateYear == theYear): #pokud počítaný rok není stejný jako rok theYear
            avYear /= dayYear
            avYear = "{:.4f}".format(avYear)
            firstDayYear[5] = avYear
            writerYear.writerow(firstDayYear)

        #PŘIDÁNÍ POSLEDNÍ ŘÁDKU SE SEDMIDENNÍM PRŮMĚREM
        if (rowNumber % 7 != 6): #pokud se nejedný o neděli jinak stejný průběh jako v podmínce v cyklu
            avSevenDay /= residueDay
            avSevenDay = "{:.4f}".format(avSevenDay)
            firstDayWeek[5] = avSevenDay
            writerWeek.writerow(firstDayWeek)
except IOError:
    print("Chybně načtený soubor")
#NAČTENÍ MAXIMÁLNÍ HODNOTY A JEJÍHO ŘÁDKU   
try:    
    with open ("Data_zelivka.csv", encoding="utf8") as csvInput:
        dataInput = csv.reader(csvInput, delimiter = ",")
        rowsmax = max(dataInput, key=lambda row: float(row[5])) #funkce max pro zjištění minima sloupce 5 (float)
        print(rowsmax)
except IOError:
    print("Chybně načtený soubor")   

    #NAČTENÍ MINIMÁLNÍ HODNOTY A JEJÁHO ŘÁDKU
try:  
    with open ("Data_zelivka.csv", encoding="utf8") as csvInput:
        dataInput = csv.reader(csvInput, delimiter = ",")
        rowsmin = min(dataInput, key=lambda row: float(row[5])) #funkce min pro zjištění minima sloupce 5 (float)
        print(rowsmin)
except IOError:
    print("Chybně načtený soubor")