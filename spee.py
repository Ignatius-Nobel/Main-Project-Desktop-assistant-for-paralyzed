import speech_recognition as sr


listenser = sr.Recognizer()
def mic():
    with sr.Microphone() as source:
        print("program is listening....")
        voice = listenser.listen(source)
        data = listenser.recognize_google(voice)
        print(data)
        return data.lower()