import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from openai import OpenAI, RateLimitError  # Import RateLimitError

import time

#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "api key address"  #api key

def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiprocess(command):
    try:
        client = OpenAI(api_key="api key address")  # Use your actual key
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message.content  # return content instead of print

    except RateLimitError:
        return "Sorry, API quota exceeded. Please check your billing."

    except Exception as e:
        return f"An error occurred: {str(e)}"

   

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://www.google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://www.facebook.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://www.linkedin.com")
   elif "open instagram" in c.lower():
      webbrowser.open("https://www.instagram.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://www.youtube.com")
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musicLibrary.music[song]
      webbrowser.open(link)
   elif "news" in c.lower():
      r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
      # Check if the request was successful
      if r.status_code == 200:

       data = r.json()
    # Print all headlines
      for article in data.get("articles", []):
        speak(article["title"])

   elif "thank you jarvis" in c.lower() or "go offline" in c.lower():
    speak("You're welcome, sir. Going offline.")
    time.sleep(1.5)  # gives audio time to play (some systems need it
    exit()  # or use `break` if you're inside a loop


   else:   # let OpenAI handle the request
      output = aiprocess(c)
      print(output)
      speak(output)

if __name__ == "__main__":
    speak("Initializing jarvis....")
    
    
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing....")
        # recognize speech using google 
        try:
            with sr.Microphone() as source:
               print("Listining.....")
               audio = r.listen(source,timeout=2, phrase_time_limit=1)  
            word = r.recognize_google(audio)
             # jarvis sprrak yes sir its mean he was activated 
            if(word.lower() == "jarvis"):
               speak("yes sir")

                              # listen for command
               with sr.Microphone() as source:
                  print("jarvis Active....")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)


                  processCommand(command)

        except Exception as e:
         print("Error; {0}".format(e))



