from record import record_voice
import os
# Use a pipeline as a high-level helper
from transformers import pipeline
speech_text = pipeline("automatic-speech-recognition", model="distil-whisper/distil-large-v3") #whisper model


def trans():
    rec_path = record_voice()
    print("path = ",rec_path)
    no_input = ["Thank You.","I'm sorry.",None,""] #ignore silent audio
    text = speech_text(rec_path)['text']  #input audio file into wisper model
    if text in no_input:
        os.remove(rec_path) #delete silent audio
    else:
        print(text)
        return text
# trans()

