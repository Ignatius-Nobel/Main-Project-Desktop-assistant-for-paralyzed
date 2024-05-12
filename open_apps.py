import os

def open_apps(query):
    if "google chrome" in query: 
        os.startfile("chrome.exe")
    elif "calculator" in query:
        os.startfile("calc.exe")
    elif "notepad" in query:
        os.startfile("notepad.exe")
    elif "edge" in query:
        os.startfile("msedge.exe")
