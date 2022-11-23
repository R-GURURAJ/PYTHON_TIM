import pyttsx3,speech_recognition as sr
import os,vlc,random


engine = pyttsx3.init()
voices = engine.setProperty("rate",170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[10].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# def hear():
#     print("ENTER AN CMD : ")
#     query = input()
#     return query


def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I AM LEASTENING........👂")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("plz wait an min.......")
        query = r.recognize_google(audio, language='en-in')
        print("YOU SAID : ", query)
    except Exception as e:
        print(e)
        speak("sorry i cant get you say it again...")
        query=hear().lower()
    return query

def rand():
    mus ="/home/guru_rio/Music/"
    fil = os.listdir(mus)
    m = random.choice(fil)
    p = vlc.MediaPlayer(f"/home/guru_rio/Music/{m}")
            
    return p

x=rand()

if __name__ == "__main__":
    while True:
        
        # x=rand()
        speak("i am lisining")
        speak("enter the cmd")
        query = hear().lower()        
        if ("play") in query:
            x.play()
        elif ("music" and "stop") in query:
            x.stop()
        elif "change" in query:
            x.stop()
            x=rand()
            x.play()