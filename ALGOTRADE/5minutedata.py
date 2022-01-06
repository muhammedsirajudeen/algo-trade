contracttotrade=input("enter the contract to be traded")
ch=int(input("enter the options to be selected \n 1.call option \n 2.put option"))
requireddata='s'
minute5_data=[]
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
                
                minute5_data.append(i['ltp'])
                T1=tuple(minute5_data)
                print(T1)
                if len(T1)==5:
                    minute_high=max(T1)
                    minute_low=min(T1)
                    
                    global minute5_data
                    minute5_data=[]
                    import csv
                    fh=open("5minutedatacall.csv","a")
                    cwriter=csv.writer(fh)
                    cwriter.writerows([[minute_high,minute_low]])
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
    #print(keyslist)
    
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
		try:

               		minute5_data.append(i['ltp'])
		except:
			print("eroor")
                T1=tuple(minute5_data)
                print(T1)
                if len(T1)==5:
                    minute_high=max(T1)
                    minute_low=min(T1)
                    
                    global minute5_data
                    minute5_data=[]
                    import csv
                    fh=open("5minutedataput.csv","a")
                    cwriter=csv.writer(fh)
                    cwriter.writerows([[minute_high,minute_low]])
                    fh.close()
                

    
        
                
    
#required data fetched successfully
    

    
    if ch==1:
        tradecalloption()

    elif ch==2:
        
        tradeputoption()
    else:
        print("error")

