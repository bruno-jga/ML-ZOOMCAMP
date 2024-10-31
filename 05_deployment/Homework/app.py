from flask import Flask, request,jsonify
from waitress import serve
import pickle

model_file="model1.bin"
dv_file='dv.bin'

with open(model_file,'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file,'rb') as dv_in:
    dv = pickle.load(dv_in)

app = Flask('APP')

@app.route('/predict', methods=['POST'])
def predict():
    customer=request.get_json()

    X=dv.transform([customer])
    y_pred=model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5

    result = {
        'probability of subscription': float(y_pred),
        'subscribed?': bool(churn)
    }

    return jsonify(result)

if __name__ == '__main__':
    serve(app,host='0.0.0.0', port=9696)