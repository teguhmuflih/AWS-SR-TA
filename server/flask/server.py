import random
import os
from flask import Flask, request, jsonify
from deploy import Keyword_Spotting_Service


# inisiasi flask app
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
	"""
	Endpoint Prediksi Kata

    :endpoint ini menggunakan file json

     Keyword = [
        	"Buka",
        	"Tutup",
    ]
	"""
	
	# mengambil file dari request POST dan menyimpannya 
	audio_file = request.files["file"]
	file_name = str(random.randint(0, 100000))
	audio_file.save(file_name)

	# inisiasi keyword spotting service  dan mendapatkan prediksi
	kss = Keyword_Spotting_Service()
	predicted_keyword = kss.predict(file_name)

	# karena sudah tidak dibutuhkan file audio, maka dihapus saja
	os.remove(file_name)

	# send back result as a json file
	# mengirim kembali hasil prediksi dalam bentuk json file
	result = {"keyword": predicted_keyword}
	return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False)


