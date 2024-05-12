# from transcribe import trans
from open_apps import open_apps
from google_search import search_about
from text_speech import speak
from play_yt import play_yt
from wiki_search import wiki
from health import health_track
from spee import mic
from mail_send import main_poc
from eye_cursor import control_mouse
from temperature import weather
from calculator import calc
import datetime
from whatsapp import sendMessage



while True:
    speak("Listening...")
    query = mic()
    # query = trans().lower()
    if query:
        # print("main-",query)
        if "open" in query:
            remove_open = query.replace("open","")
            speak(f"Opening...{remove_open} ")
            open_apps(remove_open)
        elif "search" in query:
            speak("Searching......")
            search_about(query)
        elif "play" in query:
            content_name = query.replace("play","")
            speak(f"Playing from Youtube.... {content_name}")
            play_yt(content_name)
        elif "wikipedia" in query:
            speak("Getting that from wikipedia....")
            wiki(query)
        elif "calculate" in query:
            calc(query)
        elif "my health" in query:
            health_track()
        elif "mail" in query:
            main_poc()
        elif "whatsapp" in query:
            sendMessage()
        elif "get cursor" in query:
            control_mouse()
        elif "weather in" in query:
            weather(query)
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime}")
        elif "exit" in query:
            speak("Good bye.....")
            exit()
        else:
            speak("Please repeat.......")