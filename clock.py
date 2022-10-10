from datetime import datetime
import datetime
import pyfiglet
try:
    order=str(input("alarm or stop watch or time or timer?"))

    if order=="alarm":
        while True:
            hour=int(input("enter the hour:"))
            minute=int(input("enter the minute:"))
            if minute >= 60 or hour >12:
                print("error")
            else:
                break
        while True:
            hournow=datetime.datetime.now().hour
            minutesnow=datetime.datetime.now().minute
            if hournow >12:
                hournow=hournow-12
            if hour==hournow and minute ==minutesnow:
                print("alarm on")
                break
    elif order =="stop watch":
        order1=input("when you are ready enter start:")
        if order1=="start":
            hournow=datetime.datetime.now().hour
            minutesnow=datetime.datetime.now().minute
            secondnow=datetime.datetime.now().second
            while order1=="start":
                order1=input("press any key to stop")
            newhour=datetime.datetime.now().hour
            newminutes=datetime.datetime.now().minute
            newsecond=datetime.datetime.now().second
            if newsecond<secondnow:
                newsecond=newsecond+60
                newminutes=newminutes-1
                if newminutes<minutesnow:
                    newminutes=newminutes+60
                    newhour=newhour-1
            if newminutes<minutesnow:
                newminutes=newminutes+60
                newhour=newhour-1
            time=pyfiglet.figlet_format(str(newhour-hournow)+"  :  "+str(newminutes-minutesnow)+"  :  "+str(newsecond-secondnow))
            print(time)
        else :
            print("invaild input")
    elif order=="time":
        hournow=datetime.datetime.now().hour
        minutesnow=datetime.datetime.now().minute
        secondnow=datetime.datetime.now().second
        if hournow >12:
            hournow=hournow-12
        time=pyfiglet.figlet_format(str(hournow)+"  :  "+str(minutesnow)+"  :  "+str(secondnow))
        print(time)
    elif order=="timer":
        
    
        hour=int(input("enter the hours:"))
        minute=int(input("enter the minutes:"))
        second=int(input("enter the secondes:"))
        hournow=datetime.datetime.now().hour
        minutesnow=datetime.datetime.now().minute
        secondnow=datetime.datetime.now().second
        if hournow >12:
            hournow=hournow-12
        hourwanted=hournow+hour
        minutewanted=minutesnow+minute
        seconedwanted=secondnow+second
        while seconedwanted>59 or minutewanted>59 or hourwanted>12:
            if seconedwanted>59:
                seconedwanted=seconedwanted-60
                minutewanted+=1
            if minutewanted>59:
                minutewanted-=60
                hourwanted+=1
            if hourwanted>12:
                hourwanted-=12
        
        while True:
            hournow=datetime.datetime.now().hour
            minutesnow=datetime.datetime.now().minute
            secondnow=datetime.datetime.now().second
            if (hournow-12)==hourwanted and minutesnow==minutewanted and secondnow==seconedwanted:
                break
        print("time is up")


    else:
        print("invaild input")
except:
    print("error")
