import wikipedia,string,pikachu
import webbrowser
import pyttsx3
import speech_recognition as sr,pyscreenshot as sc
import datetime,time
import os
import pyautogui,vlc,random,clock

engine = pyttsx3.init()
voices = engine.setProperty("rate",170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[10].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime("%H:%M")
    if hour >= 0 and hour < 12:
        speak(f"GOOD MORNING guru AND the time is {time}")
    elif hour >= 12 and hour < 18:
        speak(f"GOOD AFTER NOON guru AND the time is {time}")
    else:
        speak(f"GOOD EVENING guru AND the time is {time}")
    speak("what can i do for you..")


def music():
    mus ="/home/guru_rio/Music/"
    fil = os.listdir(mus)
    m = random.choice(fil)
    p = vlc.MediaPlayer(f"/home/guru_rio/Music/{m}")
            
    return p

x=music()

def log():
    hour = datetime.datetime.now()
    hour=str(hour)
    f= open("puppylog1's.txt","a+")
    f.write(hour+" :\t%s\n"%query)
    f.close
    print(hour)

def switch():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.keyUp("alt")

def screen_shot():
    x = random.random()
    y = random.random()
    time.sleep(2)
    k = sc.grab()
    k.save(f'hi{x}.png')
    print("succes")

def instaprofile():
    speak("sir please enter the insta profile name ")
    name=input("enter user name :")
    time.sleep(5)
    webbrowser.get('firefox %s').open_new_tab(f"www.instagram.com/{name}")
    speak(f"sir here is the profile of the user {name}")

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
        return hear()
    return query

# def hear():
#     print("ENTER AN CMD : ")
#     query = input()
#     return query

if __name__ == "__main__":
    wish()
    while True:
        query = hear().lower()
        log()
        if 'tim' in query:
            speak(" YES I AM ON ...WELCOME SIR..")
            while True:
                query = hear().lower()
                log()
                if 'find' in query:
                    speak("searching in wikipedia")
                    query = query.replace("find", "")
                    output = wikipedia.summary(query, sentences=5)
                    speak("GURU I HAVE FIND ..")
                    speak(output)
                    print(output)
                elif 'insta' in query:
                    instaprofile()
                elif 'open'and 'youtube' in query:
                    speak("opening youtube")
                    webbrowser.get('firefox %s').open_new_tab(f"www.youtube.com")
                elif 'open' and 'google' in query:
                    speak("opening google")
                    webbrowser.get('firefox %s').open_new_tab("google.com")
                elif ("music"and"play") in query:
                    x.play()
                elif ("change" and "music") in query:
                    x.stop()
                    x=music()
                    x.play()
                elif ('stop'and'song') in query:
                    print("stoping music")
                    x.stop()
                elif 'change window' in query:
                    switch()
                elif 'open stack overflow' in query:
                    speak("opening stark over flow")
                    webbrowser.get('firefox %s').open_new_tab("stark overflow.com")
                elif 'open vs code' in query:
                    loc = "code"
                    os.system(loc)
                elif 'pikachu' in query:
                    pikachu.mainpic()
                elif 'guru' in query:
                    loc = "/home/guru_rio/Documents/Tor"
                    os.system(loc)
                elif 'time' in query:
                    clock.mainclock()
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    speak('the time is')
                    speak(time)
                elif ("go to sleep") in query:
                    speak("i am going to sleep sir")
                    exit()
                elif 'screen shot' in query:
                    screen_shot()
                    
                elif " " in queary:
            	    continue
            	    
               elif "()" in queary:
                    speak("you said nothing..")

                else:
                    continue
        else:
            speak("the password you said is incorrect")
            print("password incorrect")
            
