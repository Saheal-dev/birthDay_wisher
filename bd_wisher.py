import pandas as pd #data manupulation and analysis 
import datetime # to get current date and time 
from plyer import notification # to  send notifications
import pyttsx3 #to speak written text 
import pywhatkit
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def notification1(title,msg):
    notification.notify(
        title= title ,
        message = msg,
       # app_icon = "D:\\birthday_wisher\\cake.png", # icon of notification
        timeout = 8
    )
    
df = pd.read_excel(r"D:\birthday_wisher\wisher.xlsx")

today = datetime.datetime.now().strftime("%d-%m")

#print(today)

for index,item in df.iterrows():
    bd= item['Birthday']
    print(bd)
    if today == bd:
        a=item["name"]
        notification1("Birthday Alert ","Its " +a+" 's birthday today.")
        speak ("sahil || Its "+a+ " 's birthday is today ")
        pywhatkit.sendwhatmsg('+918329828303','happy birthday',1,2,wait_time=5)
