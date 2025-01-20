# Personal AI Companion  

The **Personal AI Companion** is an intelligent virtual assistant designed to simplify tasks and enhance productivity. It can perform various actions such as:  
- Recognizing speech and converting it to text  
- Playing songs on YouTube  
- Sending messages on WhatsApp  
- Converting text to speech  
- Fetching the latest news headlines  
- Opening websites in the browser  

---

## Prerequisites  

To use this project, ensure you have the following installed:  
1. **Python** (version 3.6 or above)  
2. A stable internet connection for API calls and web operations  

---

## Installation  

### Step 1: Install Required Libraries  

Run the following commands to install the necessary Python modules:  

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install pywhatkit
pip install requests

Step 2: Setup News API
To enable the news functionality:

Go to News API and sign up for a free API key.
Save your API key in the news_api.txt file. This file is required for the news-fetching module to function properly.
Example of the news_api.txt file:
your_api_key_here

Usage
Key Features
Speech Recognition

The assistant can listen to your commands via the microphone and convert your speech into text.
Text-to-Speech Conversion

Using pyttsx3, the assistant provides voice responses.
Play Music on YouTube

Just command the assistant to play your favorite song, and it will open YouTube and play the track.
Send WhatsApp Messages

Use the assistant to send messages via WhatsApp with minimal effort.
Fetch News Headlines

The assistant retrieves the latest news headlines using the News API.
Open Websites

Command the assistant to open specific websites, and it will launch them in your default web browser.
Examples
Example Commands:
"Play [song name] on YouTube"
"Send a WhatsApp message to [contact]"
"What's the latest news?"
"Open [website name].com in the browser"

Contributing
Feel free to fork this repository and suggest improvements or add new features. Contributions are welcome!
