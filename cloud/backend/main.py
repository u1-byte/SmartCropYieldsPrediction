from tensorflow import keras
from flask import Flask, request, jsonify
model_location = 'test_assets/models/test_model.h5'

# input_Test_Data = [551.8,27.04,85.39,1754380.3,56.68,1.26,0.189]

app = Flask(__name__)

@app.route('/api/price_predict', methods =['GET'] )
def predict():
    data1 = float(request.args.get('param1'))
    data2 = float(request.args.get('param2'))
    data3 = float(request.args.get('param3'))
    data4 = float(request.args.get('param4'))
    data5 = float(request.args.get('param5'))
    data6 = float(request.args.get('param6'))
    data7 = float(request.args.get('param7'))
    data = [data1,data2,data3,data4,data5,data6,data7]
    print(data)
    results = {
        "harga_1":0.0,
        "harga_2":0.0,
        "harga_3":0.0,
        "harga_4":0.0
    }

    #checking input
    if len(data) != 7:
        return jsonify(str(results))
    for nilai in data:
        if str(type(nilai)) != "<class 'float'>":
            return jsonify(str(results))

    test_Model = keras.models.load_model(model_location)
    prediction = test_Model.predict([data])

    for keys,i in zip(results.keys(),prediction[0]):
        results[keys] = i

    json_results = jsonify(str(results))
    return json_results
    # print(json_results)


if __name__ == '__main__':
    app.run(debug=True)