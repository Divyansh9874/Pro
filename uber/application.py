#Backend
import numpy as np
from flask import Flask,request,render_template
import pickle
import math

application=Flask(__name__)
model=pickle.load(open('taxi.pkl','rb'))

@application.route('/')
def home():
    return render_template('index.html')
@application.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]#converting in array
    prediction=model.predict(final_features)
    output=round(prediction[0],2)
    return render_template('index.html',prediction_text="Number of Weekly Riders should be {}".format(math.floor(output)))


if __name__ == '__main__':
    application.run(debug=True)
