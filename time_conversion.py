import speech_recognition as sr
import re
import math
import time
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def au(so):
    engine.say(so)
    engine.runAndWait()

def time(iu,ou,val):   #iu= inputunit ,ou= outputunit and val= value
    if ("second" in iu) or ("seconds" in iu):
        print("sec input fun wrk")      

        if ou ==  "minute" or ou == "minutes" :
            z=str((val)/60)
            audio=(z+" minutes  ")
            print(audio)
            au(audio)
        if ou == "hour" or ou =="hours":
            print("im running")
            z=str((val)/3600)
            audio=(z+" hour")
            print(audio)
            au(audio)
        if  ou == "day" or ou == "day":
            z=str((val)/86400)
            audio=(z+ " day")
            print(audio)
            au(audio)
        if  ou == "week" or ou == "weeks" :
            z=str((val)/604800)
            audio=(z+ " week")
            print(audio)
            au(audio)
        if  ou == "month" or ou == "months":
            z=str((val)/2.628e+6)
            audio=(z + " month")
            print(audio)
            au(audio)
        if  ou =="year" or ou == "year":
            z=str((val)/ 3.154e+7)
            audio=(z+" year")
            print(audio)
            au(audio)

    elif ("minute" in iu) or ("minutes" in iu) :
        print("min input fun wrk")         
        if ou == "second" or ou ==  "seconds" :
            z=str((val)*60)
            audio=(z+" seconds")
            print(audio)
            au(audio)
        if ou == "hour" or ou =="hours":
            z=str((val)/60)
            audio=(z+" hour")
            print(audio)
            au(audio)
        if ou  == "days" or ou == "day":
            z=str((val)/1440)
            audio=(z+" day")
            print(audio)
            au(audio)
        if ou =="weeks" or ou == "week" :
            z=str((val)/10080)
            audio=(z+ " week")
            print(audio)
            au(audio)
        if iu =="months"  or ou == "month" :
            z=str((val)/43800)
            audio=(z+" month")
            print(audio)
            au(audio)
        if iu == "years"  or ou =="year" :
            z=str((val)/525600)
            audio=(z+" year")
            print(audio)
            au(audio)

    elif ("hour" in iu) or ("hours" in iu):
        print("hour input fun wrk")    

        if ou == "seconds"  or ou == "second" :
            z=str((val)*3600)
            audio=(z+" seconds")
            print(audio)
            au(audio)
        if ou == "minutes" or ou ==  "minute" :
            z = str((val)*60)
            audio=(z+" minutes  ")
            print(audio)
            au(audio)
        if ou  == "days"  or ou == "day" :
            z=str((val)/24)
            audio=(z+" day")
            print(audio)
            au(audio)
        if ou =="hour"  or ou == "hours" :
            z=str((val)/168)
            audio=(z+" week")
            print(audio)
            au(audio)
        if ou =="months"  or ou == "month" :
            z=str(((val)/730))
            audio=(z+" month")
            print(audio)
            au(audio)
        if ou == "years"  or ou =="year" :
            z=str((val)/8760)
            audio=(z+" year")
            print(audio)
            au(audio)

    elif ("day" in iu) or ("days" in iu):
        print("day input fun wrk")  
        if ou == "seconds"  or ou == "second" :
            z=str((val)*86400)
            audio=(z+" seconds")
            print(audio)
            au(audio)
            
        elif ou == "minutes"  or ou =="minute" :
            z=str((val)*1440)
            audio=(z+" minutes  ")
            print(audio)
            au(audio)

        elif ou  == "hour" or ou == "hours":
            z=str((val)*24)
            audio=(z+" hours")
            print(audio)
            au(audio)
        elif ou =="weeks"  or ou == "week" :
            z=str((val)/7)
            audio=(z+" week")
            print(audio)
            au(audio)
        elif ou == "months" or ou == "month" :
            z=str((val)/30.417)
            audio=(z+ " month")
            print(audio)
            au(audio)
        elif ou ==  "year" or ou =="year" :
            z=str((val)/0.00273973)
            audio=(z+ " year")
            print(audio)
            au(audio)
        else:
            print("Check output unit or value")
    
    elif ("week" in iu) or ("weeks" in iu):
        print("week input fun wrk")    
        if ou == "seconds"  or ou == "second" :
            z=str((val)*604800)
            audio=(z+" seconds")
            print(audio)
            au(audio)
            
        if ou == "minutes"  or ou =="minute" :
            z=str((val)*10080)
            audio=(z+" minutes  ")
            print(audio)
            au(audio)
        if ou  == "hours" or ou == "hour":
            z=str((val)*168)
            audio=(z+ "hours")
            print(audio)
            au(audio)
        if ou =="days" or ou ==  "day":
            z=str((val)*7)
            audio=(z+" days")
            print(audio)
            au(audio)
        if ou =="months"  or ou == "month" :
            z=str((val)/4.345)
            audio=(z+" month")
            print(audio)
            au(audio)
        if ou == "years"  or ou =="year" :
            z=str((val)/52.143)
            audio=(z+"year")
            print(audio)
            au(audio)
            
    elif ("month" in iu) or ("months" in iu):
        print("month input fun wrk")    
        if ou == "seconds" or ou == "second" :
            z=str((val)*2.628e+6)
            audio=(z+" seconds")
            print(audio)
            au(audio)
        
        if ou == "minutes"  or ou =="minute" :
            z=str((val)*43800)
            audio=(z+" minutes  ")
            print(audio)
            au(audio)
        if ou  == "hours"  or ou == "hour":
            z=str((val)*730)
            audio=(z+"hours")
            print(audio)
            au(audio)
        if ou =="days"  or ou ==  "day":
            z=str((val)*30)
            audio=(z+"days")
            print(audio)
            au(audio)
        if iu =="weeks"  or ou == "week" :
            z=str((val)/4)
            audio=(z+" weeks")
            print(audio)
            au(audio)
        if iu == "years" or ou =="year" :
            z=str((val)/12)
            audio=(z+" year")
            print(audio)
            au(audio)
    
    elif ("year" in iu) or ("years" in iu):
        print("year input fun wrk")    
        if ou == "seconds" or ou == "second" :
            z=str((val)*3.154e+7)
            audio=(z+" second")
            print(audio)
            au(audio)
            
        if ou == "minutes"  or ou =="minute" :
            z=str((val)*525600)
            audio=(z+" minutes  ")
            print(audio)
            au(audio)
        if ou  == "hours"  or ou == "hour":
            z=str((val)*8760)
            audio=(z+" hours")
            print(audio)
            au(audio)
        if ou =="days"  or ou ==  "day":
            z=str((val)*365)
            audio=(z+" days")
            print(audio)
            au(audio)
        if ou =="weeks" or ou == "week" :
            z=(val)*52.1429
            audio=(z+" weeks")
            print(audio)
            au(audio)
        if ou == "months"  or ou =="month" :
            z=str((val)*12)
            audio=(z+" months")
            print(audio)
            au(audio)
        else:
            ("wrng output unit or value")
    else:
        print("check the input unit")

if __name__ == "__main__":

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Plz say convert time :")
        audio = r.listen(source)
        try:
            outstr= r.recognize_google(audio)
            print("You said : {}".format(outstr))
            a=str(outstr)
            temp = re.findall(r'\d+', a)
            lenth=len(temp)
            if "half"  in a:
                g=a.split()
                outputunit=g[-1]
                print(outputunit)
                foriu=g[:-1]
                chng=a.replace("half", ".30",)
                print(chng)
                final = " ".join(re.findall(r"[0-9.]+", chng))
                val=final.replace(" ", "",)
                inputunit="hour"
                time(inputunit,outputunit,float(val))             
                
      
   

            elif (":" in a) and (lenth==2):
                g=a.split()
                outputuni=g[-1]
                print(outputunit)
                delforiu=g[:-1]
                str1 = " "
                foriu = (str1.join(delforiu))
                chng=a.replace(":", ".",)
                print(chng)
                final = " ".join(re.findall(r"[0-9.]+", chng))
                val=final.replace(" ", "",)
                if "minute" or "minutes" in foriu:
                    inputunit="hour"
                    time(inputunit,outputunit,float(val)) 
            
            elif lenth==2:
                g=a.split()
                outputunit=g[-1]
                inputunit="hour"
                print("output unit : {}".format(outputunit))
                removestr = " ".join(re.findall(r"[0-9]+", a))
                val=removestr.replace(" ", ".",)
                print("value : {}".format(val))
                print("input unit : {}".format(inputunit))
                time(inputunit,outputunit,float(val))


                
            else:
                #a="convert 1 seconds to hour"
                g=a.split()
                outputunit=g[-1]
                print("output unit : {}".format(outputunit))
                delforiu=g[:-1]
                str1 = " "
                foriu = (str1.join(delforiu))
                print(foriu)
                final = " ".join(re.findall(r"[0-9]+", a))
                z=(final.rstrip())
                print("value : {}".format(z))
                print("input unit : {}".format(foriu))
                time(foriu,outputunit,int(final))
                


        except:
            print("Sorry could not recognize your voice")
    

