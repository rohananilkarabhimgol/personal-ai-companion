import os
import speech_recognition as sr
import pyttsx3
import webbrowser


# Initializing the text-to-speech engine
engine = pyttsx3.init()

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
         

if __name__ == "__main__":
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
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process_command(command)

            print("Google Speech Recognition thinks you said " + command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

