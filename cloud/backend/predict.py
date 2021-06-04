import database.query as query

def pred_temp():
    input_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]  # need to change this
    output_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]
    input_scaler = MinMaxScaler()
    output_scaler = MinMaxScaler()
    input_scaler.fit(input_fit_data)
    output_scaler.fit(output_fit_data)

    temp_3, temp_2, temp_1, temp_0 = query.get_temp()
    temp = [[temp_3, temp_2, temp_1, temp_0]]

    input_data = input_scaler.transform(temp)
    raw_prediction = test_Model.predict(input_data)
    prediction = output_scaler.inverse_transform(raw_prediction)

    temp_out = prediction[0]
    json_results = jsonify(temp_out)
    return json_results

def pred_hum():
    input_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]  # need to change this
    output_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]
    input_scaler = MinMaxScaler()
    output_scaler = MinMaxScaler()
    input_scaler.fit(input_fit_data)
    output_scaler.fit(output_fit_data)

    hum_3, hum_2, hum_1, hum_0 = query.get_hum()
    hum = [[hum_3, hum_2, hum_1, hum_0]]

    input_data = input_scaler.transform(hum)
    raw_prediction = test_Model.predict(input_data)
    prediction = output_scaler.inverse_transform(raw_prediction)

    hum_out = prediction[0]
    json_results = jsonify(hum_out)
    return json_results

def pred_rain():
    input_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]  # need to change this
    output_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]
    input_scaler = MinMaxScaler()
    output_scaler = MinMaxScaler()
    input_scaler.fit(input_fit_data)
    output_scaler.fit(output_fit_data)

    rain_3, rain_2, rain_1, rain_0 = query.get_rain()
    rain = [[rain_3, rain_2, rain_1, rain_0]]

    input_data = input_scaler.transform(rain)
    raw_prediction = test_Model.predict(input_data)
    prediction = output_scaler.inverse_transform(raw_prediction)

    rain_out = prediction[0]
    json_results = jsonify(rain_out)
    return json_results

def pred_shine():
    input_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]  # need to change this
    output_fit_data = [[26.49, 26.49, 26.49, 26.49],
                      [30.25, 30.25, 30.25, 30.25]]
    input_scaler = MinMaxScaler()
    output_scaler = MinMaxScaler()
    input_scaler.fit(input_fit_data)
    output_scaler.fit(output_fit_data)

    shine_3, shine_2, shine_1, shine_0 = query.get_shine()
    shine = [[shine_3, shine_2, shine_1, shine_0]]

    input_data = input_scaler.transform(shine)
    raw_prediction = test_Model.predict(input_data)
    prediction = output_scaler.inverse_transform(raw_prediction)

    shine_out = prediction[0]
    json_results = jsonify(shine_out)
    return json_results