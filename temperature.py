import requests
from text_speech import speak

def weather(query):
    query = query.replace("weather in","")
    query = query.replace(" ","")
    query = query.replace(".","")
    API_Key = "0b2f398b968df0acfb3768f66d7c442f"
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={API_Key}&units=metric")
    temp = weather_data.json()['main']['temp']
    temp_round = int(temp)
    print(temp)
    speak(f"The weather is {temp_round}  degree celcius")
# weather("kerala")