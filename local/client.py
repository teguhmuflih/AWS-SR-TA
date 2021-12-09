import requests

# server url
URL = "http://54.172.4.83/predict"
#URL = "http://54.89.85.190:500/predict"
#URL = "http://http:/127.0.0.1:5000/predict"

# audio file we'd like to send for predicting keyword
#FILE_PATH = r"C:\Users\HARDWARE\Desktop\Kodingan Akhir\AWS-SR-TA\local\test\Aldi_buka_50cm.wav"
FILE_PATH = r"C:\Users\HARDWARE\Desktop\Kodingan Akhir\AWS-SR-TA\local\test\Ayu_tutup_50cm (5).wav"


if __name__ == "__main__":

    # open files
    file = open(FILE_PATH, "rb")

    # package stuff to send and perform POST request
    values = {"file": (FILE_PATH, file, "audio/wav")}
    response = requests.post(URL, files=values)
    data = response.json()

    print(f"Prediksi kata: {data['keyword']}")
