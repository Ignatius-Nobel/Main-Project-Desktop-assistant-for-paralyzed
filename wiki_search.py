import wikipedia
from text_speech import speak
def wiki(query):
    query = query.replace("wikipedia","")
    result = wikipedia.summary(query,sentences=2)
    speak("According to wikipedia...")
    speak(result)