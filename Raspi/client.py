import requests
import sounddevice as sd
from scipy.io.wavfile import write
import RPi.GPIO as GPIO # import General Purpose Input / Output
import time 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT, initial=GPIO.HIGH) # pada Relay menggunakan pin 
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # pada LED
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # pada pushbutton

# server url
URL = "http://18.233.162.14/predict"
# Lokasi suara dalam format .wav
FILE_PATH = r"output.wav"

fs = 44100 # Sample rate
seconds = 2  # Durasi

def record():
    print("record.....")
    GPIO.output(11, True)
    time.sleep(0.5)
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write('output.wav', fs, myrecording)  # Menyimpan dalam bentuk WAV

    GPIO.output(11, False)
    print("stop")

if __name__ == "__main__":
    #Merekam menggunakan mikrofon
    while True:
        button_state = GPIO.input(8)
        if button_state == False:
            print("Tombol ditekan...")
            record()

            # membuka files
            file = open(FILE_PATH, "rb")

            # mengirim dengan metode POST
            values = {"file": (FILE_PATH, file, "audio/wav")}
            response = requests.post(URL, files=values)
            data = response.json()

            print(f"Prediksi kata: {data['keyword']}")
            if data['keyword'] == 'Buka' :
                GPIO.output(3, False) # Relay membuka kunci pintu
                time.sleep(3)
                # time.sleep(15) # 2 menit
                GPIO.output(3, True)
            else :
                GPIO.output(3, True) # Relay menutup kunci pintu
                time.sleep(0.3)

