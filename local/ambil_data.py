import requests

# server url
URL = "http://54.172.4.83/predict"



if __name__ == "__main__":

    # open files
    response = requests.get(URL)
    data = response.json()

    print(f"Prediksi kata: {data['keyword']}")