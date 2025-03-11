from flask import Flask, render_template, request
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open('diabetes_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        input_data = [float(request.form[i]) for i in request.form]

        # Convert input to NumPy array and scale it
        input_data = np.array(input_data).reshape(1, -1)
        input_data_scaled = scaler.transform(input_data)

        # Make a prediction
        prediction = model.predict(input_data_scaled)
        result = "Diabetic 😢" if prediction[0] == 1 else "Not Diabetic 😊"
        
        return render_template('result.html', prediction=result)

    except Exception as e:
        return render_template('result.html', prediction="Error: Invalid Input")

if __name__ == '__main__':
    app.run(debug=True)
