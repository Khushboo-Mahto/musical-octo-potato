import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")  

    speak(" Iam Jarvish . please tell me how may i help you")  

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language= 'en-in')
        print(f"user said : {query}\n")

    except Exception as e :
        # print(e)
        print("say that again please....")
        return "None"

    return query

if __name__ == "__main__":
    # speak("Ram is a good boy")

    wishMe()
    # takeCommand()

    while True :
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace('wikipedia', "")
            result= wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
         
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Khushboo Mahto\\Desktop\\Songs'

            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"sir, the time is {strtime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\Khushboo Mahto\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'

            os.startfile(codePath)


        