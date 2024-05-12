import pyttsx3

# Initialize the TTS engine
def speak(text):
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 170)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
