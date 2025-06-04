from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained classification model
model = pickle.load(open('C:\\Users\\harsh\\OneDrive\\Desktop\\edunet\\model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values
        pressure = float(request.form['pressure'])
        dewpoint = float(request.form['dewpoint'])
        humidity = float(request.form['humidity'])
        cloud = float(request.form['cloud'])
        sunshine = float(request.form['sunshine'])
        winddirection = float(request.form['winddirection'])
        windspeed = float(request.form['windspeed'])

        # Prepare input for model
        input_data = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])

        # Predict class: 0 or 1
        prediction = model.predict(input_data)[0]

        # Interpret prediction
        result = "Rainfall" if prediction == 1 else "No Rainfall"

        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
