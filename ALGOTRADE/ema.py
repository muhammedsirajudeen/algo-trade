import time
import csv
while True:
    closelist=[]
    emalist=[]
    
    time.sleep(1)
    with open("emapoints.csv","r") as fh:
        creader=csv.reader(fh)
        
        for minute5_close in creader:
            closelist.append(minute5_close)
        

        #print(rec)

            
        multiplier=0.333333333
        print(multiplier)
        constant=1.0
        with open("ema.csv","r") as fh:
            ereader=csv.reader(fh)
            for ema in ereader:
                emalist.append(ema)

            #print("The previous Ema is",ema)
    
#length of total closes
    totalcloses=len(closelist)-1
    unpuri_finalclose=closelist[totalcloses]
    for i in unpuri_finalclose:
        singlefinalclose=float(i)


    totalema=len(emalist)-1
    unpuri_finalema=emalist[totalema]
    for i in unpuri_finalema:
        lastrecema=float(i)
    currentema=singlefinalclose*multiplier+lastrecema*(constant-multiplier)


    with open("ema.csv","a") as fh:
        ewriter=csv.writer(fh)
        emadata=[
            [currentema]]
        ewriter.writerows(emadata)
        fh.close()
        
