import csv

        
            
with open ("Data_zelivka.csv", encoding="utf8") as csvZelivkaInput,\
    open("data_parkoviste_out.csv", "w", encoding="utf8") as csvoutfile:
    dataInput = csv.reader(csvZelivkaInput, delimiter = ",")
    writer = csv.writer(csvoutfile)
    for row in dataInput:  
        try:
            print(row[0],row[1],row[2],row[3],row[4],float(row[5]))
        except ValueError:
            pass

    
