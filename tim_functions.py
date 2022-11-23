import wikipedia
import webbrowser
import random
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyscreenshot as sc
import time



engine = pyttsx3.init()
voices = engine.setProperty("rate",189)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I AM LEASTENING........👂")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("plz wait an min.......")
        queary = r.recognize_google(audio, language='en-in')
        print("YOU SAID : ", queary)

    except:
        print("USER SAID: NULL")                
        return hear()
    return queary
    


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"GOOD MORNING guru AND the time is {hour}")
        speak("IT IS GOING TO BE AN GOOD DAY FOR YOU")
    elif hour >= 12 and hour < 18:
        speak(f"GOOD AFTER NOON guru AND the time is {hour}")
        speak("HI GURU HOW WAS THE MORNING ")
    else:
        speak(f"GOOD EVENING guru AND the time is {hour}")
        speak("I THINK TIS IS AN AWESOME DAY FOR YOU ")
    speak("what can i do for you..")

def music():
    import os
    import random
    mus = "D:\\GURU\\MUSIC"
    fil = os.listdir(mus)
    m = random.choice(fil)
    os.startfile(os.path.join(mus, m))
    speak(m)
    print("success")

def screen_shot():
    x = random.random()
    time.sleep(2)
    k = sc.grab()
    k.save(f'hi{x}.png')
    print("succes")