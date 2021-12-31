import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):#it is used to perform text to speech conversion.
    engine.say(text)
    engine.runAndWait()

def wish():#wish user sccording to time.
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("hello sweet heart   i am your assistant  please tell me how may i help you?")

def take():#it takes microphone input and returns a string output.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        r.energy_threshold=250
        text=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(text)
        print(query)

    except Exception as e:
        print(e)
        print("say that again please...")
        return  "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("ttme564@gmail.com",'mlp0nko9')
    server.sendmail("ttme564@gmail.com",to,content)
    server.close()


if __name__ == '__main__':
    wish()
    while True:
        query=take().lower()

        if "wikipedia" in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening Youtube...")
            query=query.replace("youtube","")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open('youtube.com')

        elif 'open google' in query:
            speak("opening google...")
            query=query.replace("google","")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open('google.com')

        elif 'open geek for geeks' in query:
            speak("opening geekforgeeks...")
            query=query.replace("geekforgeeks","")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open('geekforgeeks.com')

        elif 'open gmail' in query:
            speak("opening gmail...")
            query=query.replace("gmail","")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open('gmail.com')

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir the time is{strtime}")
            speak(f"sir the time is{strtime}")

        elif 'open vs' in query:
            speak("opening vs code")
            vspath="C:\\Users\\divya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)

        elif 'open pycharm' in query:
            speak("opening pycharm")
            pcpath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(pcpath)

        elif 'mail to' in query:
            try:
                speak("Sir What should i say?")
                content=take()
                to="divynsh943bharadwaj@gmail.com"
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                print("Sorry sir,there is some issue in sending mail")

        elif 'quit' or 'exit' in query:
            exit()
