import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()  # initializes the pyttsx3 modules
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
new_speak_rate = 150
engine.setProperty('rate', new_speak_rate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# speak("Hello World! I am Totto . How can I help you?")


def time():
    time_now = datetime.datetime.now().strftime("%H : %M : %S")
    speak(time_now)


def date():
    year = datetime.datetime.now().year  # Extracts current year
    mon = datetime.datetime.now().month  # Extracts current month
    day = datetime.datetime.now().day  # Extracts current day
    speak("Current date is")
    speak(day)
    speak(mon)
    speak(year)


def wishme():
    # speak("Hello Sir!")
    # time()
    # date()
    hour = datetime.datetime.now().hour

    if 6 <= hour <= 12:
        speak("Good morning sir")
    elif 12 < hour <= 15:
        speak("good afternoon sir")
    elif 16 < hour <= 24:
        speak("Good evening sir")
    else:
        speak("good Night sir")

    speak("Totto is at your service")


# wishme()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, 'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Could you please repeat again")
        return "none"


takeCommand()






