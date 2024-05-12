from text_speech import speak
import pywhatkit
import wikipedia as googleScrap

def search_about(query):
    query = query.replace("search","")
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        speak("This is what i found for you....")
        speak(result)
    except:
        speak("No information found!!!")






