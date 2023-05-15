import pickle
import tensorflow as tf
import test_data_preprocessing
import numpy as np
import statistics
import warnings
warnings.filterwarnings("ignore")


def main(website):
    # Selecting the best performed models
    ml_model_names = ["model_svm", "model_dt"]
    em_model_names = ["model_cb", "model_gb"]
    dl_model_names = ["model_rnn", "model_mlp"]

    # Loading the preprocess test data
    test_data = test_data_preprocessing.main(website)

    # Converting the test data into 2d and 3d arrays to evaluate the trained models
    test_data_2d = test_data.reshape(-1, test_data.shape[-1])
    test_data_3d = test_data_2d.reshape(-1, 1, test_data_2d.shape[1])

    # creating an empty array to store the results
    results = {}

    # Loading and getting prediction from machine learning models
    for name in ml_model_names:
        with open(f"ml_models/{name}.pkl", "rb") as f:
            model = pickle.load(f)
            # Getting the prediction from the models
            prediction = model.predict([test_data])
            results[name] = int(prediction)

    # Loading and getting prediction from ensemble learning models
    for name in em_model_names:
        with open(f"em_models/{name}.pkl", "rb") as f:
            model = pickle.load(f)
            # Getting the prediction from the models
            prediction = model.predict([test_data])
            results[name] = int(prediction)

    # Setting the probability threshold value to get binary prediction from deep learning models
    threshold = 0.5

    # Loading and getting prediction from deep learning models
    for name in dl_model_names:
        if name == "model_mlp":
            with open(f"dl_models/{name}.pkl", "rb") as f:
                model = pickle.load(f)
                # Getting the prediction from the models
                prediction = model.predict([test_data])
                binary_prediction = np.where(prediction >= threshold, 1, 0)
                results[name] = int(binary_prediction)
        else:
            loaded_model = tf.keras.models.load_model(f"dl_models/{name}.h5")
            # Getting the prediction from the models
            prediction = loaded_model.predict(test_data_3d)
            binary_prediction = np.where(prediction >= threshold, 1, 0)
            results[name] = int(binary_prediction)

    # Get the values (results) from the dictionary
    values = list(results.values())

    # Calculate the mode of the data
    mode = statistics.mode(values)

    if mode == 1:
        return "Phishing"
    elif mode == 0:
        return "Legetimate"
