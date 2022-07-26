import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import pyjokes
# import smtplib
# import cv2
from userinfo import *
from sys_dir_files import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def jarvis(speak):
    engine.say(speak)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        jarvis("Good Morning!")

    elif hour>=12 and hour<18:
        jarvis("Good Afternoon!")   

    else:
        jarvis("Good Evening!")  

    # jarvis("tell me how may I help you")   

def takeorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('started.. you can speak now..')
        r.pause_threshold = 0.5
        rec_order = r.listen(source)
        try:
            print('recognizing ur order')
            order = r.recognize_google(rec_order)
            order = order.lower()
            if 'jarvis' in order:
                order = order.replace('jarvis','')
                print(order)
                return order
            else:
                print(order)
                return order
            
        except Exception as e:
            print(e)
            print('something went wrong! say it again')
            return 'None'
 
def whatsappmessage_timer():
    now = datetime.datetime.now()
    hr = now.strftime("%H")
    mini =now.strftime("%M")
    t_min= mini
    t_min = int(t_min)+1
    li = [hr,t_min]
    return li
    
if __name__=="__main__" :
    # cap = cv2.VideoCapture(0)
    # _,img = cap.read()
    greeting()
    while True:
        order = takeorder()
        #start the jarvis answer based on questions
        if 'wikipedia' in order:
            jarvis('searching wikipedia')
            # order = order.replace("wikipedia", "")
            print(order)
            results = wikipedia.summary(order, sentences=2)
            jarvis('According to wikipedia')
            print(results)
            jarvis(results)
        elif 'what is your name' in order and 'name' in order:
            jarvis('Hi my name is JARVIS')
        elif 'play' in order and 'youtube' in order:
            # order = order.replace("youtube","")
            # order = order.replace("play","")
            print(order)
            jarvis('opening youtube')
            pywhatkit.playonyt(order)
        elif 'open google' in order:
            jarvis('opening google chrome')
            webbrowser.open(google)
        elif 'open youtube' in order:
            jarvis('opening youtube')
            webbrowser.open('youtube.com') 
        elif 'open github' in order:
            jarvis('opening github')
            webbrowser.open(githubacct)
        elif 'open gmail' in order or 'open mail' in order:
            jarvis('opening gmail')
            webbrowser.open(gmail)
        elif 'open google chrome' in order or 'open chrome' in order:
            jarvis('opening google chrome')
            webbrowser.open(google)
        elif 'open spotify' in order:
            jarvis('opening spotify')
            os.startfile(spotify)
        elif 'play some music' in order or 'play music' in order or 'play song' in order:
            jarvis('opening music')
            webbrowser.open(spotifyweb)
        elif 'time now' in order or 'whats time' in order or 'time' in order:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(now)
            jarvis(now) 
        elif 'open code editor' in order or 'open vs code' in order or 'open visual studio' in order:
            jarvis('opening code editior')
            os.startfile(vscode)
        elif 'send message in whatsapp' in order or 'message in whatsapp' in order:
            jarvis('ok whom to send message')
            person = takeorder()
            if person == 'None' or person == ' ' or person == '' or person==None:
                jarvis("say again. whom to send message")
                person = takeorder()
            
            person = person.replace(" ","")
            if person in contact:
                number = contact[person]
                jarvis('whats message')
                message = takeorder()
            else:
                jarvis(person+' number')
                number = takeorder()
                number = '+91'+number
                number = number.replace(" ","")
                jarvis('whats message')
                message = takeorder()
            timer = whatsappmessage_timer()    
            print(f'number = {number}, message = {message}')
            pywhatkit.sendwhatmsg(number,message,int(timer[0]),int(timer[1]))
            jarvis('message sent successfully')
        elif 'what is' in order or 'search what is' in order:
            jarvis('searching')
            print(order)
            pywhatkit.search(order)
        elif 'create a folder' in order or 'create folder' in order:
            jarvis('folder name')
            dic_name  = takeorder()
            dic_name = dic_name.replace(" ","")
            parentdic = "C:/Users/syedsyed/Desktop"
            path = os.path.join(parentdic, dic_name)
            print(path)
            os.mkdir(path)
            jarvis('created successfully')
        elif 'joke' in order:
            jarvis(pyjokes.get_joke())
        elif 'shutdown' in order and 'system' in order:
            os.system("shutdown /s /t 1")
        elif 'close google window' in order or 'close chrome' in order or 'close chrome window' in order:
            os.system("taskkill /im chrome.exe /f")
        elif 'close work tabs' in order or 'close window tabs' in order or 'close all tabs' in order:
            os.system("taskkill /im chrome.exe /f")
            os.system("taskkill /im Code.exe /f")
        elif 'hey' in order or 'hi' in order or 'how are you' in order or 'hay' in order or 'hai' in order :
            jarvis('hi, am great. how may i help you')
        
            
            
