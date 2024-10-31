import pickle
from flask import Flask, request,jsonify
from waitress import serve

model_file='M05_deployment\Notes\model.bin'

with open(model_file,'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('Churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer=request.get_json()

    X=dv.transform([customer])
    y_pred=model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=9696)