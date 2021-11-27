import csv
from typing import IO

#NAČTENÍ DAT A ZÁKLADNÍ OPERACE  
try:
    with open ("vstup.csv", encoding="utf8") as csvInput,\
        open("vystup_7dni.csv","w", encoding="utf8") as csvOutputWeek,\
        open("vystup_rok.csv","w", encoding="utf8") as csvOutputYear:
        dataInput = csv.reader(csvInput, delimiter = ",")
        writerWeek = csv.writer(csvOutputWeek)   
        writerYear = csv.writer(csvOutputYear)  
        
        #DEFINICE POMOCNÝCH PROMĚNNÝCH 
        rowNumber = 0
        avSevenDay = 0
        residueDay = 0
        dayYear = 0
        avYear = 0
        maxCurrent = 0
        minCurrent = float("inf")
        
        #CYKLUS ČTOUCÍ ŘÁDKY VSTUPU
        for row in dataInput:     
            if rowNumber % 7 == 0: #výběr prvního dne sedmidenního rozsahu 
                firstDayWeek = row     
            if dataInput.line_num == 1: #výběr prvního dne roku
                firstDayYear = row
                calculateYear = int(firstDayYear[2])  #pouze úprava na int
            theYear = int(row[2]) #zápis druhého sloupce do roku (bez int)
            residueDay += 1 
            #ZÁPIS DO SOUBORU S ROČNÍMI HODNOTAMI
            if theYear != calculateYear:
                avYear /= dayYear #průměr za rok
                firstDayYear[5] = "{:.4f}".format(avYear) 
                writerYear.writerow(firstDayYear) #zápis do souboru
                firstDayYear = row
                calculateYear = int(firstDayYear[2])
                avYear = 0 #vynulování před znovu-projetím cyklu
                dayYear = 0
            dayYear += 1
            try:
                avSevenDay += float(row[5]) #suma dní v týdnu
                avYear += float(row[5]) #suma dní v týdnu
                theDay = float(row[5]) #pomocná hodnota pro výpis největšího a nejmenšího řádku
            except ValueError:
                print("Na řádku ",dataInput.line_num ," je chybně zadaná hodnota, a proto nedisponuje ve výpočtu průměrů") #výjimka neodstraní celý řádek (neustále existence při opakování 7 dní)
            except IndexError:
                print("Na řádku ",dataInput.line_num ," je nesprávně dlouhé pole, a proto nedisponuje ve výpočtu průměrů") #výjimka neodstraní celý řádek (neustále existence při opakování 7 dní)
            #ZÁPIS DO SOUBORU SE SEDMIDENNÍMI HODNOTAMI
            if (rowNumber % 7 == 6):
                avSevenDay /= 7
                firstDayWeek[5] = "{:.4f}".format(avSevenDay)   #formátování na 4 desetinná místa
                writerWeek.writerow(firstDayWeek)
                residueDay = 0
                avSevenDay = 0    #vynulování před znovu-projetím cyklu
            #VÝPOČET MAXIMA A MINIMA
            if (theDay > float(maxCurrent)):
                maxValue = row
                maxCurrent = row[5]
            if (theDay < float(minCurrent) and theDay > 0):
                minValue = row
                minCurrent = row[5]
            
            #VÝPIS NEKORETNÍCH DAT
            if (theDay <= 0):
                wrongValue = row
                print("Řádek se zápornou či nulovou hodnotou je",dataInput.line_num,":\n",wrongValue)
              
            rowNumber += 1
        #PŘIDÁNÍ POSLEDNÍHO ŘÁDKU S ROČNÍM PRŮMĚREM
        avYear /= dayYear
        avYear = "{:.4f}".format(avYear)
        firstDayYear[5] = avYear
        writerYear.writerow(firstDayYear)

        #PŘIDÁNÍ POSLEDNÍHO ŘÁDKU SE SEDMIDENNÍM PRŮMĚREM
        if (rowNumber % 7 != 0): #pokud se nejedný o neděli jinak stejný průběh jako v podmínce v cyklu
            avSevenDay /= residueDay      
            avSevenDay = "{:.4f}".format(avSevenDay)
            firstDayWeek[5] = avSevenDay
            writerWeek.writerow(firstDayWeek)
        print(f"Maximální hodnota průtoku nastala {maxValue[4]}.{maxValue[3]}.{maxValue[2]} a dosahovala hodnoty: {maxValue[5]}.")
        print(f"Minimální hodnota průtoku nastala {minValue[4]}.{minValue[3]}.{minValue[2]} a dosahovala hodnoty: {minValue[5]}.")
    
        
except IOError: #výjimka při načtení souboru
    print("Chybně načtený soubor")
