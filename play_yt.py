import webbrowser
import pywhatkit

def play_yt(query):
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(web)