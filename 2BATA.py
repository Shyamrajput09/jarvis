import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os

engine=pyttsx3.init()
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)

    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("Iam  BATA AI SIR . lease tell me how I can help you")
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"Usear said: {query}")
    except Exception as e:
        # speak("say that again please....")
        print("say that again please....")
        return "None"
    return query
    
# if __name__ == "__main__":

wishMe()
while True:
   
    query= takecommand().lower()
        
    if 'wikipedia' in query:
        speak('Searching in Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'youtube' in query:
            webbrowser.open("youtube.com")
    elif 'google' in query:
            webbrowser.open("google.com")
    elif 'instagram' in query:
            command_path="C:\\Users\\shyam\\OneDrive\\Desktop\\Instagram.lnk"
            os.startfile(command_path)
            
    elif 'tcs self service' in query:
            webbrowser.open("tcsion.com")
    elif 'tcs' in query:
            webbrowser.open("https://g01.tcsion.com/LX/Dashboard")
    elif 'canva' in query:
            command_path="C:\\Users\\shyam\\OneDrive\\Desktop\\Canva.lnk"
            os.startfile(command_path)
    elif 'amazon' in query:
            webbrowser.open("amazon.in")
    elif 'flipcart' in query:
            webbrowser.open("flipcart.com")
    elif 'jiocinema' in query:
            webbrowser.open("jiocinema.com")
    elif 'chess' in query:
            webbrowser.open("chess.com")
    elif 'whatsapp' in query:
            command_path="C:\\Users\\shyam\\OneDrive\\Desktop\\WhatsApp Web.lnk"
            os.startfile(command_path)
            
    elif 'power point' in query:
            command_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(command_path)
    elif 'excel' in query:
             command_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
             os.startfile(command_path)
    elif 'ms word' in query:
             command_path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
             os.startfile(command_path)
    elif 'Physics Walla' in query:
             command_path="C:\\Users\\shyam\\OneDrive\\Desktop\\Physics Wallah.lnk"
             os.startfile(command_path)
    elif 'stop' in query:
            break
            