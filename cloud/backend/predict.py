import database.query as query
import h5py
import gcsfs

from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from flask import jsonify

FS = gcsfs.GCSFileSystem(
        project='Smart Crop Yields Prediction', token='test_assets/cred.json')

def predict(input_fd,output_fd,get_input,model_location):
    input_scaler = MinMaxScaler()
    output_scaler = MinMaxScaler()
    input_scaler.fit(input_fd)
    output_scaler.fit(output_fd)
    # print(get_input)
    input = [get_input]

    with FS.open(model_location, 'rb') as model_file:
        model_gcs = h5py.File(model_file, 'r')
        model = keras.models.load_model(model_gcs)

    input_data = input_scaler.transform(input)
    raw_prediction = model.predict(input_data)
    scaled_prediction = output_scaler.inverse_transform(raw_prediction)
    prediction = scaled_prediction[0]
    
    return prediction


def pred_temp():
    input_fit_data = [[26.49, 26.49, 26.49, 26.49, 26.49, 26.49, 26.49, 26.49, 26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25, 30.25, 30.25, 30.25, 30.25, 30.25, 30.25, 30.25, 30.25]]  # need to change this
    output_fit_data = [[26.49, 26.49, 26.49, 26.49],
                       [30.25, 30.25, 30.25, 30.25]]
    
    model_location = 'gs://rice_price_dev/ml_models/temp_model.h5'

    prediction = predict(input_fit_data,output_fit_data,query.get_temp(),model_location)
    json_results = jsonify(prediction)
    return json_results


def pred_hum():
    input_fit_data = [[67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0, 67.0],
                      [85.45, 85.45, 85.45, 85.45, 85.45, 85.45, 85.45, 85.45, 85.45, 85.45, 85.45, 85.45]]  # need to change this
    output_fit_data = [[67.0, 67.0, 67.0, 67.0],
                       [85.45, 85.45, 85.45, 85.45]]

    model_location = 'gs://rice_price_dev/ml_models/hum_model.h5'

    prediction = predict(input_fit_data,output_fit_data,query.get_hum(),model_location)
    json_results = jsonify(prediction)
    return json_results


def pred_rain():
    input_fit_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [21.84, 21.84, 21.84, 21.84, 21.84, 21.84, 21.84, 21.84, 21.84, 21.84, 21.84, 21.84]]  # need to change this
    output_fit_data = [[0, 0, 0, 0],
                       [21.84, 21.84, 21.84, 21.84]]
    
    model_location = 'gs://rice_price_dev/ml_models/rain_model.h5'

    prediction = predict(input_fit_data,output_fit_data,query.get_rain(),model_location)
    json_results = jsonify(prediction)
    return json_results


def pred_shine():
    input_fit_data = [[3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27],
                      [9.47, 9.47, 9.47, 9.47, 9.47, 9.47, 9.47, 9.47, 9.47, 9.47, 9.47, 9.47]]  # need to change this
    output_fit_data = [[3.27, 3.27, 3.27, 3.27],
                       [9.47, 9.47, 9.47, 9.47]]
    
    model_location = 'gs://rice_price_dev/ml_models/shine_model.h5'

    prediction = predict(input_fit_data,output_fit_data,query.get_shine(),model_location)
    json_results = jsonify(prediction)
    return json_results

print(pred_shine())