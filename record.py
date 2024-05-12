import pyaudio
import wave
import time

def rec_time():
    millisec = int(round(time.time() * 1000))
    return millisec
def record_voice():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    OUTPUT_FOLDER = "audio_rec"  # Folder to save the audio file
    voice_time = str(rec_time())+ ".wav"
    WAVE_OUTPUT_FILENAME = f"aud_rec\{voice_time}"


    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(WAVE_OUTPUT_FILENAME)
    return WAVE_OUTPUT_FILENAME
# record_voice()