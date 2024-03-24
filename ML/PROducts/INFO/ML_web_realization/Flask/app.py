from catboost import CatBoostClassifier
import numpy as np
from flask import Flask, render_template,request
import pickle
import joblib
import webview
import sklearn

app = Flask(__name__)
model = pickle.load(open('Подготовка1_model.pkl', 'rb'))
window = webview.create_window('Predictions!',app)
@app.route('/' , methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    min_max = joblib.load('scaler_age_bmi_HbA1c_glucose.joblib')
    min_max_nums = min_max.transform(np.array([int_features[1],int_features[5],int_features[6],int_features[7]]).reshape(1, -1))
    int_features[1] = min_max_nums[0][0]
    int_features[5] = min_max_nums[0][1]
    int_features[6] = min_max_nums[0][2]
    int_features[7] = min_max_nums[0][3]
    final_features = [np.array(int_features)]
    slovar = {0:'Not diabetic',1:'Diabetic'}
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text='Prediction: {}'.format(slovar[prediction[0]]))

if __name__ == "__main__":
    # app.run(debug=True)
    webview.start()