#  we have to make two threads one take intraday ltp of given contract every second
import threading
import time
def data_collection():
    
    contracttotrade=input("enter the contract to be traded")
    ch=int(input("enter the options to be selected \n 1.call option \n 2.put option"))
    high_lowdata=[]
    countlist=[]


    while True:
    
    #import time
    #time.sleep(1)
        def tradecalloption():
    
        
        

#THIS PROGRAM IS TO COLLECT TIC DATA AND ON THE PROCESS CALCULATING HIGH AND LOW OF CERTAIN PERIODS

            import urllib, json
            import ast
            import unicodedata
            url = "https://groww.in/v1/api/option_chain_service/v1/option_chain/nifty?expiry=2021-12-02"
            response = urllib.urlopen(url)
            data = json.loads(response.read())
#data collected from api
            calloption={}
            putoption={}
            calloptionlist=[]
            putoptionlist=[]
#objects for later use

#print(data)
            with open('price.json', 'w') as f:
   #data=strip(data)
                json.dump(data, f,indent=4)
                f.close()
                print(type(data))
                for i in data:
                    pass
                    for j in data["optionChains"]:
            
            
                        calloption=dict(j['callOption'])
                        putoption=dict(j['putOption'])
            #now most of the process is over and we have
            #cleansed the data
            #now taking required ones is pretty easy
                        calloptionlist.append(calloption)
                        putoptionlist.append(putoption)

#data cleansed successfully
            count=0
            keyslist=[]
            finaldictionary={}
            finaldictionarylist=[]
            for i in calloptionlist:
    #print(i)
    
                calloptionkeys=i.keys()
    #print(calloptionkeys)
    
    

                keyslist=[calloptionkeys[1],calloptionkeys[6],calloptionkeys[10]
                  ,calloptionkeys[11],calloptionkeys[12],calloptionkeys[14]]
    #print(keyslist)
    
            count=0
            for i in calloptionlist:
                finaldictionary={calloptionkeys[1]:i[calloptionkeys[1]]
                         ,calloptionkeys[11]:i[calloptionkeys[11]]}
                finaldictionarylist.append(finaldictionary)

#print(finaldictionarylist)
            for i in finaldictionarylist:
    #print(i)
                c=i
                finaldictionarylist.remove(c)



            for i in finaldictionarylist:
                if i['growwContractId']==contracttotrade:
                    
                    try:
                        
                    
                        last1_price=i['ltp']
                        #print(last1_price)
                    except:
                        print("error")
                    
                        
                    
                    import csv
                    with open('5minutedatacall.csv','r') as fh:
                        creader=csv.reader(fh)
                        trading_data=[]
                        for rec in creader:
                            trading_data.append(rec)
                        high_low=len(trading_data)-1
                        highlow_data=trading_data[high_low]
                        global high_data
                        global low_data
                        high_data=int(highlow_data[0])
                        low_data=int(highlow_data[1])
                    with open('ema.csv','r') as fh:
                        creader=csv.reader(fh)
                        emadata=[]
                        for rec in creader:
                            emadata.append(rec)
                        ema_index=len(emadata)-1
                        ema_data=emadata[ema_index]
                        pure_ema=int(ema_data[0])
                        
                        
                        import csv
                        fh=open('tradingcriteriacall.csv','a')
                        ewriter=csv.writer(fh)
                        ewriter.writerows(
                            [[pure_ema,high_data,low_data,last1_price]])
                        fh.close()
                        
                        

                
                    

                                
                        
                    
                    
                        
    
                

    
                

        def tradeputoption():
        
        

#final process in data fetching put this as a function that runs
#in the required intervals to collect the close or last traded price
#then we can use the collected data to draw charts or build strategies
#process 1 completed-datafetchedsuccessfully
#process 2 writing code as a function that executes itself in 5 minute interval and collect data-which is easy
#process 3 writing code for trading strategy -pending
#process 4 writing code to execute the trade using python and selenium-pending
#process 4-building gui and charts to help while backtesting-pending

            import urllib, json
            import ast
            import unicodedata
            url = "https://groww.in/v1/api/option_chain_service/v1/option_chain/nifty?expiry=2021-12-02"
            response = urllib.urlopen(url)
            data = json.loads(response.read())
#data collected from api
            calloption={}
            putoption={}
            calloptionlist=[]
            putoptionlist=[]
            print("1st part")
#objects for later use

#print(data)
            with open('price.json', 'w') as f:
   #data=strip(data)
                json.dump(data, f,indent=4)
                f.close()
            #print(type(data))
                for i in data:
                    L=30
                    for j in data["optionChains"]:
            
            
                        calloption=dict(j['callOption'])
                        putoption=dict(j['putOption'])
            #now most of the process is over and we have
            #cleansed the data
            #now taking required ones is pretty easy
                        calloptionlist.append(calloption)
                        putoptionlist.append(putoption)

            print("2ndd part")

#data cleansed successfully
            count=0
            keyslist=[]
            finaldictionary={}
            finaldictionarylist=[]
            for i in putoptionlist:
    #print(i)
    
                putoptionkeys=i.keys()
    #print(calloptionkeys)
    
    

                keyslist=[putoptionkeys[1],putoptionkeys[6],putoptionkeys[10]
                  ,putoptionkeys[11],putoptionkeys[12],putoptionkeys[14]]
    #print(keysist)
    
            count=0
            for i in putoptionlist:
            
            
                finaldictionary={putoptionkeys[1]:i[putoptionkeys[1]],putoptionkeys[11]:i[putoptionkeys[11]]}
            
            
                finaldictionarylist.append(finaldictionary)
            
#print(finaldictionarylist)
#print(finaldictionarylist)
            for i in finaldictionarylist:
    #print(i)
                c=i
                finaldictionarylist.remove(c)
        


            for i in finaldictionarylist:
                if i['growwContractId']==contracttotrade:
                    print(i)
                    last_price=i['ltp']
                    
                    import csv
                    with open('5minutedatacall.csv','r') as fh:
                        creader=csv.reader(fh)
                        trading_data=[]
                        for rec in creader:
                            trading_data.append(rec)
                        high_low=len(trading_data)-1
                        highlow_data=trading_data[high_low]
                        high_data=int(highlow_data[0])
                        low_data=int(highlow_data[1])
                    with open('ema.csv','r') as fh:
                        creader=csv.reader(fh)
                        emadata=[]
                        for rec in creader:
                            emadata.append(rec)
                        ema_index=len(emadata)-1
                        ema_data=emadata[ema_index]
                        pure_ema=int(ema_data[0])
                        print(pure_ema)
                        print(high_data)
                        print(low_data)
                        import csv
                        fh=open('tradingcriteriaput.csv','a')
                        ewriter=csv.writer(fh)
                        ewriter.writerows(
                            [[pure_ema,high_data,low_data,last_price]])
                        fh.close()

            
        
        #the last problem faced by me is
        #here i have to make a way that the function only reads
        #from the file if it has new line
        
        
        
        
                
                

    
        
                
    
#required data fetched successfully
    

    
        if ch==1:
            tradecalloption()

        elif ch==2:
            
            last_pricedata=tradeputoption()
        else:
            print("error")

t1=threading.Thread(target=data_collection)

t1.start()

def trading():
    
    
        time.sleep(4)
    
        ch=1
    
        
        def call():
            
            while True:
                loop=0
                import csv
                fh=open('tradingcriteriacall.csv','r')
                creader=csv.reader(fh)
                trading_data=[]
                for m in creader:
                    trading_data.append(m)
                    
                data_index=len(trading_data)-1
                unpuri_data=trading_data[data_index]
                ema_data=int(unpuri_data[0])
                high_data=int(unpuri_data[1])
                low_data=int(unpuri_data[2])
                
                last_price=float(unpuri_data[3])
                print("waiting for trade")
                
                
                
                if (low_data-ema_data)>0:
                    if (low_data-ema_data)>9:
                        stoploss=high_data
                        entry=low_data
                        while True:
                            
                            if loop==1:
                                break
                            if last_price<=entry:
                                print("entered the trade")
                                print("entry at",last_price)
                            
                                
                                    
                                
                                while True:
                                    import csv
                                    mh=open('tradingcriteriacall.csv','r')
                                    kreader=csv.reader(mh)
                                    price1_data=[]
                                    for z in kreader:
                                        price1_data.append(z)
                                    
                                    price_index=len(price1_data)-1
                                    unpuri1_price=price1_data[price_index]
                                    last_price1data=float(unpuri1_price[3])
                                    
                                    print("#######################",last_price1data)
                                    if last_price1data>=stoploss:
                                        print("sold the trade as it hit stop loss",stoploss)
                                        
                                        loop=1
                                        break
                                    if last_price1data<=ema_data:
                                        print("sold the trade as it reached our target",ema_data)
                                        
                                        loop=1
                                        break


                
        def put():
            
            
            while True:
                
                
                import csv
                fh=open('tradingcriteriaput.csv','r')
                creader=csv.reader(fh)
                trading_data=[]
                for m in creader:
                    trading_data.append(m)
                    
                data_index=len(trading_data)-1
                unpuri_data=trading_data[data_index]
                ema_data=int(unpuri_data[0])
                high_data=int(unpuri_data[1])
                low_data=int(unpuri_data[2])
                last_price=float(unpuri_data[3])
                
                if (low_data-ema_data)>0:
                    if (low_data-ema_data)>9:
                        stoploss=high_data
                        entry=low_data
                        if last_price<=entry:
                            
                            print("entered the trade")
                            print("entry at",entry)
                            while True:
                                import csv
                                lh=open('tradingcriteriaput.csv','r')
                                mreader=csv.reader(lh)
                                price_data=[]
                                for k in mreader:
                                    price_data.append(k)
                                price_index=len(price_data)-1
                                unpuri_price=price_data[price_index]
                                last_pricedata=float(unpuri_price[3])
                                print("nested loops price data",last_pricedata)
                                print(stoploss)
                                if last_pricedata>=stoploss:
                                    print("sold the trade as it hit stop loss",stoploss)
                                if last_pricedata==ema_data:
                                    print("sold the trade as it reached our target",ema)

                
        if ch==1:
            call()
        else:
            put()
t2=threading.Thread(target=trading)
t2.start()


