import requests
import sounddevice as sd
from scipy.io.wavfile import write

# server url
URL = "http://54.172.4.83/predict"
# Lokasi suara dalam format .wav
FILE_PATH = r"output.wav"

fs = 44100  # Sample rate
seconds = 3  # Durasi

def record():
    print("record.....")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  
    write('output.wav', fs, myrecording)  # Menyimpan dalam bentuk WAV
    print("stop")

if __name__ == "__main__":
    #Merekam menggunakan mikrofon
    record()

    # open files
    file = open(FILE_PATH, "rb")

    # package stuff to send and perform POST request
    values = {"file": (FILE_PATH, file, "audio/wav")}
    response = requests.post(URL, files=values)
    data = response.json()

    print(f"Prediksi kata: {data['keyword']}")
