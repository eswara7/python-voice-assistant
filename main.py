import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio
listener =sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 
engine.say("helllo")
engine.say("How may i help you")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def get_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'google' in command:
                command=command.replace('hey google' , '')
                print(command)
                #talk(command)
    except:
        pass
    return command

def run_google():
    command=get_command()
    #print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)
        talk("playing")
    elif 'search' in command:
        s=command.replace('search','')
        pywhatkit.search(s)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('the present time is ' +time)
    elif "who is" in command:
        person=command.replace("who is",'')
        getinfo=wikipedia.summary(person,1)
        print(getinfo)
        talk(getinfo)
    elif "what is" in command:
        thing=command.replace("what is",'')
        ginfo=wikipedia.summary(thing,2)
        #print(ginfo)
        talk(ginfo)
    elif "i love you" in command:
        talk("sorry i have a relationship with eeswar")
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "gurram" in command:
        talk("gurram is bad boy")
    elif "are you single" in command:
        talk("no i love eeswar")
   
    elif 'who are you' in command:
        talk("i am your google assistant")
    elif 'do you like to talk with siri' in command:
        talk("i don't really,but i do actually") 
        
    elif 'bye' in command:
        talk("thank you see you again")
        exit(1)
    else:
        talk("sorry say it again")

while True:
    run_google()
