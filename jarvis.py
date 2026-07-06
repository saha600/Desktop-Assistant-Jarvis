
import pyttsx3
import datetime
import webbrowser
import pywhatkit
import pyjokes
import pyautogui
import os

engine = pyttsx3.init()
engine.setProperty("rate",170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def wish():
    h=datetime.datetime.now().hour
    if h<12:
        speak("Good Morning!")
    elif h<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you?")

wish()

while True:
    command=input("\nEnter Command: ").lower().strip()

    if "time" in command:
        speak("The time is "+datetime.datetime.now().strftime("%I:%M %p"))

    elif "date" in command:
        speak("Today's date is "+datetime.datetime.now().strftime("%d %B %Y"))

    elif "google" in command and "search" not in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command and not command.startswith("play"):
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command.startswith("search"):
        q=command.replace("search","",1).strip()
        if q:
            speak("Searching Google")
            webbrowser.open("https://www.google.com/search?q="+q)
        else:
            speak("Please enter a search term.")

    elif "wikipedia" in command:
        topic=command.replace("wikipedia","",1).strip()
        if topic:
            speak("Opening Wikipedia")
            webbrowser.open("https://en.wikipedia.org/wiki/"+topic.replace(" ","_"))
        else:
            speak("Please enter a topic.")

    elif command.startswith("play"):
        song=command.replace("play","",1).strip()
        if song:
            speak("Playing "+song)
            pywhatkit.playonyt(song)
        else:
            speak("Please enter a song name.")

    elif "joke" in command:
        joke=pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "paint" in command:
        speak("Opening Paint")
        os.system("mspaint")

    elif "command prompt" in command or command=="cmd":
        speak("Opening Command Prompt")
        os.system("start cmd")

    elif "file explorer" in command or "explorer" in command:
        speak("Opening File Explorer")
        os.system("explorer")

    elif "screenshot" in command:
        speak("Taking screenshot")
        img=pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot saved.")

    elif command in ("exit","bye"):
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I did not understand that command.")
