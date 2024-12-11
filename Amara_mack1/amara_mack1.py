import  _tkinter as tk
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("I am your amara mack 1")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            listener.pause_threshold = 1
            voice = listener.listen(source, timeout = 5, phrase_time_limit = 6)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "amara" in command:
                command = command.replace("amara", "")
                print(command)

    except:
        pass
    return command

def run_amara():
    command = take_command()
    print(command)

    #Action to "play" on YouTube

    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    #Action to tell the time

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%m %p")
        print(time)
        talk("current time is" + time)

    #Action to search for on wikipedia

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
while True:
    run_amara()







    #except Exception as e:
    #   print(f"system not working: {e}")