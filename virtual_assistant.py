import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import json
import requests

''' NEWS API'''
newsapi = open("news_api.txt","r").read()
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

# Initializing the text-to-speech engine
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 130)     # setting up new voice rate

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# Function to convert text to speech and play it aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process voice commands
def process_command(c):
    # Condition to open a web application in the browser
    if c.lower().startswith("open"):
        webapp_name = c.replace("open","").strip()
        webbrowser.open(f"https://www.{webapp_name}.com")

    # Condition to play music on YouTube
    elif c.lower().startswith("play"):
        song_name = c.replace("play","").strip()
        speak(f"playing {song_name} on youtube")
        if song_name:
            pywhatkit.playonyt(song_name)
        else:
            speak("No song found")
    # Condition to send message on whatsapp
    elif "send whatsapp message" in c.lower(): 
        name = c.replace("send whatsapp message to","").strip
        pywhatkit.sendwhatmsg(name, "Hi")
        webbrowser.open(f"https://www.whatsapp.com")
         
    # Fetching news throw an api key
    elif "news" in c.lower():
        response = requests.get(url)
        # Check if the request was sucessfull
        
        if response.status_code == 200:
            # Parsing the JSON response
            data = response.json()

            # Extracting the articles
            articals = data.get('articles',[])

            # Printing the articles
            for artical in articals :
                speak(artical['title'])

        else:
            speak(f"Failed to retrive the headline! {response.status_code}")


if __name__ == "__main__":
    speak("Activating assistant")
    while True:
        # Obtaining audio input from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            command =  r.recognize_google(audio)

            # Activating the system upon a specific wake word or trigger
            if "assistant" in command.lower():
                speak("How can i help you")
                with sr.Microphone() as source:
                    print("Listning....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process_command(command)

            print("Google Speech Recognition thinks you said " + command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

