import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
import os
# from gtts import gTTS
# import pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsAPI = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3')
    
#     # initialize pygame mixer
#     pygame.mixer.init()
    
#     # load the mp3 file
#     pygame.mixer.music.load('temp.mp3')

#     # play the mp3 file
#     pygame.mixer.music.play()
    
#     # keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
        
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")
    
# def aiCommand(command):
#     genai.configure(api_key="AIzaSyDRgnpT6plIwp-93bu2i3erKYcLPfjqXGU")

#     model = genai.GenerativeModel('gemini-1.5-flash')

#     response = model.generate_content(command)
#     return response.text

    
def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com/in/adarsh-raj-vats2002/")
        
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        print("Searching for song")
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsAPI}")
        # Check if the request was successful
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
        else:
            speak(f"Failed to retrieve news articles. Status code: {r.status_code}")
            
    else:
        # It's time for openAI to handle the requests
        # output = aiCommand(command)
        # speak(output)
        speak("Please try again, I wasn't able to listen to you properly!")
        
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen to the wake word "Jarvis"
        # obtain audio from the microphone
        
        r = sr.Recognizer()

        # recognize speech using Sphinx - we won't do as its not perfect, so we'll use google
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes master")
                #listening to the command 
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
                    
        except Exception as e:
            print("Error; {0}".format(e))
