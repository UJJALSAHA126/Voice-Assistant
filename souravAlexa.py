import speech_recognition as sr
import pyttsx3
import pywhatkit


listener = sr.Recognizer()
en = pyttsx3.init()

voices = en.getProperty('voices')
en.setProperty('voice',voices[1].id)
def talk(text) :
    en.say(text)
    en.runAndWait()

def take_command() :
    try:
        with sr.Microphone() as source :
            # print("Speak Now.....")
            # voice= listener.listen(source)
            # command = listener.recognize_google(voice)
            command = "alexa play java"
            talk(command)
            return command
    except:
        pass    

def run_alexa() :
    # command = take_command()
    # if 'play' in command :
    song = "Code With Harry"
    talk(song)
    pywhatkit.playonyt(song)

run_alexa()