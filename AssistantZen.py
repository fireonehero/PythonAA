import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import os
from datetime import date, datetime
import random
import webbrowser
import youtubesearchpython
import wikipedia

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

r = sr.Recognizer()

summonPhrase = "off"

amount_failed = 0

jokelist = [
    'What did the traffic light say to the car? Don’t look! I’m about to change.',
    'Today at the bank, an old lady asked me to help check her balance. So I pushed her over.',
    'My boss told me to have a good day.. so I went home.',
    "I couldn't figure out why the baseball kept getting larger. Then it hit me.",
    'What did one plate whisper to the other plate? Dinner is on me.',
    "Why did the old man fall in the well? Because he couldn't see that well.",
    'I know a lot of jokes about unemployed people but none of them work.',
    'My wife told me I had to stop acting like a flamingo. So I had to put my foot down.',
    "The other day, my wife asked me to pass her lipstick but I accidentally passed her a glue stick. She still isn't talking to me.",
    'Why is Peter Pan always flying? He neverlands.'
]

tellingjoke = random.choice(jokelist)

responselist = [
    'Yes',
    'At your command',
    'As you wish',
    'Your wish is my command',
    'Yes sir',
    'It shall be done',
    'Sure thing'
]

responsephrase = random.choice(responselist)

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.09)
        print('Listening : ')
        audio = r.listen(source)
        print(datetime.now().strftime("%I %M %p"))
        try:
            words = r.recognize_google(audio).lower()
            print('You said : {}'. format(words))     
                
            if words.__contains__ ("power on"):
                speak("Yes")
                summonPhrase = "on"

            if summonPhrase == "on":

                #Date/Time
                if words.__contains__("what is the date"):
                    speak(date.today().strftime("%B %d, %Y"))    

                elif words.__contains__("what time is it"):
                    speak("The time is:" + datetime.now().strftime("%I:%M %p"))


                #Joke
                elif words.__contains__("tell me a joke"):
                    speak(tellingjoke)

                #Opening Stuff
                elif words.__contains__("play the song"):
                    speak(responsephrase)
                    words = 'yes ' + words
                    webbrowser.open(f'https://www.youtube.com/watch?v=' + youtubesearchpython.VideosSearch(words.split('play the song')[1], limit = 2).result()['result'][0]['id'])

                elif words.__contains__("open youtube"):
                    webbrowser.open("https://www.youtube.com")

                elif words.__contains__("search for"):
                    better_words = words.replace("search for", " ")
                    webbrowser.open(f"https://duckduckgo.com/?t=ffab&q=" + better_words)

                elif words.__contains__("anime time"):
                    webbrowser.open("https://9anime.to/home")

                elif words.__contains__("open reddit"):
                    webbrowser.open("https://www.reddit.com")

                #Searching Wikipedia
                elif words.__contains__("search wikipedia for"):
                    best_words = words.replace("search wikipedia for", " ")
                    speak(wikipedia.summary(best_words, sentences = 5))

                #Description
                elif words.__contains__("what do you do"):
                    speak(f"""I am Zen, your custom made Artificial Assistant, I currently have 11 commands at my disposal.""")


                #Killing the bot
                elif words.__contains__("kill the bot"):
                    speak("Killing it now.")
                    os._exit(0)
                
                #Poweringoff the bot
                elif words.__contains__("power off"):
                    speak(responsephrase)
                    summonPhrase = "off"

        except:
            print("Retrying it")