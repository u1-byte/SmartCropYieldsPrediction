import json
from tensorflow import keras
model_location = 'test_assets/models/test_model.h5'

# input_Test_Data = [551.8,27.04,85.39,1754380.3,56.68,1.26,0.189]

def predict(data):

    results = {
        "harga_1":0.0,
        "harga_2":0.0,
        "harga_3":0.0,
        "harga_4":0.0
    }

    #checking input
    if len(data) != 7:
        return json.dumps(str(results))
    for nilai in data:
        if str(type(nilai)) != "<class 'float'>":
            return json.dumps(str(results))

    test_Model = keras.models.load_model(model_location)
    prediction = test_Model.predict([data])

    for keys,i in zip(results.keys(),prediction[0]):
        results[keys] = i

    json_results = json.dumps(str(results))
    return json_results
    # print(json_results)
