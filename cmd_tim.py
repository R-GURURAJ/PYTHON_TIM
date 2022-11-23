import wikipedia
import tim_functions
import webbrowser
import pyttsx3
import datetime
import os

# engine = pyttsx3.init()
# voices = engine.setProperty("rate",170)
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[10].id)
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    time = (datetime.datetime.now().strftime("%H:%M"))
    if hour >= 0 and hour < 12:
        speak(f"GOOD MORNING guru AND the time is {time}")
    elif hour >= 12 and hour < 18:
        speak(f"GOOD AFTER NOON guru AND the time is {time}")
    else:
        speak(f"GOOD EVENING guru AND the time is {time}")
    speak("what can i do for you..")

def music():
   import os,random
   mus ="C:/Users/Student/Downloads/Michael Schuller - Motivational Inspirational Cinematic Trailer.mp3"
#    for multiple files
#    fil = os.listdir(mus)
#    m = random.choice(fil)
   os.startfile(mus)
   print("success")

def hear():
    print("ENTER AN CMD : ")
    query = str(input())
    return query

if __name__ == "__main__":
    wish()
    
    while True:
        query = hear()
        if 'tim' in query:
            speak(" YES I AM ON ....experting for command...")
            while True:
                print("hhh")
                query = hear()
                chrome_path ="C:/Users/Student/AppData/Local/Google/Chrome/Application/chrome.exe %s"
                # C:\Users\Student\AppData\Local\Google\Chrome\Application
                
                if 'find' in query:
                    speak("searching in wikipedia")
                    query = query.replace("find", "")
                    output = wikipedia.summary(query, sentences=5)
                    speak("GURU I HAVE FIND ..")
                    speak(output)
                    print(output)
                     
                elif 'open youtube' in query:
                    speak("opening youtube")
                    webbrowser.get(chrome_path).open("youtube.com")
                     
                elif 'open google' in query:
                    speak("opening google")
                    webbrowser.get(chrome_path).open("google.com")
                     
                elif 'open stack over flow' in query:
                    speak("opening stack over flow")
                    print(chrome_path)
                    webbrowser.get(chrome_path).open("https://stackoverflow.com/")
                     
                elif 'open vs code' in query:
                    loc = "C:/Users/Student/AppData/Local/Programs/Microsoft VS Code/Code"
                    os.startfile(loc)
                     
                elif 'time' in query:
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    speak("the time is "+time)
                elif 'exploer' in query:
                    import pyautogui as pg
                    pg.hotkey('win', 'e')

                elif 'stop' in query:
                    quit()
                    
                elif 'music' in query:
                    music()
                    
                elif 'vlc' in query:
                   os.system("vlc")

                elif 'screen shot' in query:
                    tim_functions.screen_shot()
                else:
                    print("\n\n ",query," is not an cmd")
                    continue 
                
        else:
            speak("you are not the owner !")
            print("permission denied")
