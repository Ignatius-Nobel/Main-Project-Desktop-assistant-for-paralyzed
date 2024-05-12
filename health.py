import requests
from text_speech import speak

def health_track():
    url = "https://v1.nocodeapi.com/ignatius_nobel123/fit/KdtikMyEobwUyclY/aggregatesDatasets?dataTypeName=heart_minutes,weight&timePeriod=today"
    params = {}
    r = requests.get(url = url, params = params)
    result = r.json()['weight'][0]['value']
    speak(f"Your heart rate is {result}bpm")
    print(result)
# health_track()