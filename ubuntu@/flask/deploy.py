import librosa
import tensorflow as tf
import numpy as np

SAVED_MODEL_PATH = "model_manual_dataset.h5"
SAMPLES_TO_CONSIDER = 22050

class _Keyword_Spotting_Service:
    
    model = None
    _mapping = [
        "Buka",
        "Tutup",
    ]
    _instance = None


    def predict(self, file_path):

        # Ekstraksi MFCC
        MFCCs = self.preprocess(file_path)

        # Membutuhkan 4 Dimensi untuj prediksi: (# samples, # time steps, # coefficients, 1)
        MFCCs = MFCCs[np.newaxis, ...]

        # mendapatkan prediksi label
        predictions = self.model.predict(MFCCs)
        predicted_index = np.argmax(predictions)
        predicted_keyword = self._mapping[predicted_index]
        return predicted_keyword


    def preprocess(self, file_path, num_mfcc=13, n_fft=2048, hop_length=512):
        # memuat file audio
        signal, sample_rate = librosa.load(file_path)

        if len(signal) >= SAMPLES_TO_CONSIDER:
            # memastikan konsistensi data audio
            signal = signal[:SAMPLES_TO_CONSIDER]

            # Ekstraksi MFCC
            MFCCs = librosa.feature.mfcc(signal, sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                         hop_length=hop_length)
        return MFCCs.T


def Keyword_Spotting_Service():
    # ensure an instance is created only the first time the factory function is called
    if _Keyword_Spotting_Service._instance is None:
        _Keyword_Spotting_Service._instance = _Keyword_Spotting_Service()
        _Keyword_Spotting_Service.model = tf.keras.models.load_model(SAVED_MODEL_PATH)
    return _Keyword_Spotting_Service._instance


if __name__ == "__main__":
    # membuat 2 instance dari keyword spotting service
    kss = Keyword_Spotting_Service()
    kss1 = Keyword_Spotting_Service()

    # check that different instances of the keyword spotting service point back to the same object (singleton)
    assert kss is kss1

    # make a prediction
    keyword = kss.predict(r"local\test\Aldi_buka_50cm.wav")
    print(keyword)

    # make a prediction
    keyword2 = kss1.predict(r"local\test\Ayu_tutup_50cm (5).wav")
    print(keyword2)