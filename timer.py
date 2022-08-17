import datetime
import os
from playsound import playsound

#logic
def alarmf(syear,smon,sdate,shour,smin,ssec,ampm):
    print('-------------')
    print('Time set to',shour,':',smin,':',ssec,'  ', ampm,' on  ',sdate,'-',smon,'-',syear)
    print('-------------')
    print('Message is ready to sent')
    print('-------------')
    while(1):
       x=datetime.datetime.now()
       if(x.hour==shour and x.minute==smin and x.second==ssec and   x.day==sdate and x.month==smon and  x.year==syear):
          print('Message Successfully Sent on ',x)
          playsound('C:\\Users\\konda\\Music\\Beast_Bgm.mp3')
          continuef()

#leapyear fun()
def leapf(syear):
     if(syear%4==0 and syear%100!=0 or syear%400==0):
         return 1
     else:
         return 0

#for continution
def continuef():
    to_continue=input('Want to continue:')
    if(to_continue=='yes'):
        os.system('clear')
        mainf()
    else:
        exit()
#for termination
def terminatef():
    print('Enter Correct time')
    continuef()
      
#date and month decision
def mondatef(smon,sdate,leap):
    if(smon==1 or smon==3 or smon==5 or smon==7 or smon==8 or smon==10 or smon==12):
        if(sdate>31):
            terminatef()
    elif(smon==2 and leap==1):
            if(sdate>29):
                terminatef()
    elif(smon==2 and leap==0):
            if(sdate>28):
                terminatef()
    elif(smon==2 or smon==4 or smon==6 or smon==9 or smon==11):
            if(sdate>30):
                terminatef()
    else:
         terminatef()
       
#For Input Date and Time
def inputf():
    x=datetime.datetime.now()
    print('\tDATE AND TIME:')
    date=list(map(int,input("Enter Date(date/month/year):").split('/')))
    time=list(map(int,input("Enter Time(hours:minutes:seconds):").split(':')))
    ampm=input('am or pm:')#am or pm
    syear=date[2]#year
    leap=leapf(syear)#leapyear function
    if(syear<x.year):#year termination
        terminatef()
    else:
      smon=date[1]#month
      if((syear==x.year and smon<x.month) or smon>12 or (smon<=0 or smon>12)):# month termination
          terminatef()
      else:
          sdate=date[0]#date
          mondatef(smon,sdate,leap)#month and date check function
          if((syear==x.year and smon==x.month and sdate<x.day) or sdate<0):#date termination
                terminatef()
          else:
                shour=time[0]#hours
                if(shour<0 and shour>12):
                    terminatef()
                if(ampm=='pm' and shour!=12):
                    shour=shour+12
                if((sdate==x.day and shour<x.hour) or shour<0 or shour>23):#hours termination
                    terminatef()
                else:
                    smin=time[1]#minutes
                    if((smin<x.minute and shour==x.hour) or smin<0  or smin>59):#minutes termination
                        terminatef()
                    else:
                        ssec=time[2]#seconds
                        if((ssec<x.second and smin==x.min) or ssec<0 or ssec>59):#seconds termination
                            terminatef()
                        else:
                            alarmf(syear,smon,sdate,shour,smin,ssec,ampm)


def mainf():
    try:
        inputf()      
    except Exception as e:
        print(e,'is the Exception')
        continuef()
        
#mainfunction   
mainf()  

