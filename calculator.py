import wolframalpha
from text_speech import speak
requester = wolframalpha.Client('XUKET9-HH848KTAJY')
def calc(query):
    
    query = query.replace("calculate","")
    query = str(query)
    if query:
        requested = requester.query(query)

        try:
            answer = next(requested.results).text
            print(str(answer))
            speak(f"The result is {answer}")
        except:
            speak("The value is not answerable")
    else:
        speak("Please Repeat!!!!")

# calc("2+3")

