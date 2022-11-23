import wikipedia
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    speak("HI EVERY ONE ")


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"GOOD MORNING guru AND the time is {hour}")
    elif hour >= 12 and hour < 18:
        speak(f"GOOD AFTER NOON guru AND the time is {hour}")
    else:
        speak(f"GOOD EVENING guru AND the time is {hour}")
    speak("what can i do for you..")


def music():
    import random,vlc
    mus = " path "
    fil = os.listdir(mus)
    m = random.choice(fil)
    p = vlc.MediaPlayer(f" path /{m}")
    p.play()
    print("success")


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
    return query


if __name__ == "__main__":
   wish()

   while True:
      query = hear().lower()
      if 'david' in query:
         speak(" YES SIR I AM ON ....,")
         while True:
            query = hear().lower()
            if 'find' in query:

              speak("searching in wikipedia")

              query = query.replace("find", "")

              output = wikipedia.summary(query, sentences=2)

              speak("GURU I HAVE FIND ..")

              speak(output)

              print(output)

              break

            elif 'open youtube' in query:

              speak("opening youtube")

              webbrowser.open("youtube.com")

              break

            elif 'open google' in query:

              speak("opening google")

              webbrowser.open("google.com")

              break

            elif 'open starkoverflow' in query:

              speak("opening stark over flow")

              webbrowser.open("stark overflow.com")

              break

            elif 'open pc' in query:
                speak("opening pc ")
                pat = "This PC"
                os.startfile(pat)
                break

            elif 'open vs code' in query:
                speak("opening vs code")

                loc = " "

                os.startfile(loc)

                break

            elif 'time' in query:

              time = datetime.datetime.now().strftime("%H:%M:%S")

              speak(time)

              break

            elif 'stop' in query:

               quit()


            elif 'music' in query:

               music()

               break
      
            elif 'exit' in query:
               exit()
      else:
            speak("say the correct password")
            continue
         
