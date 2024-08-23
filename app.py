from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from function_transform import transform_list
import pickle

app = Flask(__name__)

model = load_model('model/churn_model_new.keras')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        data = [
            request.form.get('gender'),
            request.form.get('SeniorCitizen'),
            request.form.get('Partner'),
            request.form.get('Dependents'),
            request.form.get('tenure'),
            request.form.get('PhoneService'),
            request.form.get('MultipleLines'),
            request.form.get('OnlineSecurity'),
            request.form.get('OnlineBackup'),
            request.form.get('DeviceProtection'),
            request.form.get('TechSupport'),
            request.form.get('StreamingTV'),
            request.form.get('StreamingMovies'),
            request.form.get('PaperlessBilling'),
            request.form.get('MonthlyCharges'),
            request.form.get('TotalCharges'),
            request.form.get('InternetService'),
            request.form.get('Contract'),
            request.form.get('PaymentMethod')
            
        ]
        
        print(data)

        # Convert form data to the appropriate types
        preprocessed_data = transform_list(data)
        
       

        print(preprocessed_data)
    

        input_data = np.array(preprocessed_data).reshape(1,-1)

        # Make prediction
        prediction = model.predict(input_data)
        result = "Churn" if prediction[0][0] > 0.5 else "No Churn"

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
