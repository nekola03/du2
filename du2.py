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
        max = 0
        min = 10000
        
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
                theDay = float(row[5]) #pomocná hodnota pro výpis největšího a nejmenšího řádku
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
            #VÝPOČET MAXIMA A MINIMA
            if (theDay > float(max)):
                maxValue = row
                max = row[5]
            if (theDay < float(min)):
                minValue = row
                min = row[5]
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
        print(maxValue)
        print(minValue)
except IOError: #výjimka při načtení souboru
    print("Chybně načtený soubor")
