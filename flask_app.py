from flask import Flask, jsonify, request
import pathlib
import pickle
from train import do_train

cwd = pathlib.Path.cwd

app = Flask(__name__)
app.config['DEBUG'] = True

model = pickle.load(open('ad_model.pkl','rb'))

@app.route('/api/v1/predict', methods=['GET'])
def predict():
    
    tv = request.args.get('tv', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    if tv is None or radio is None or newspaper is None:
        return "Args empty, the data are not enough to predict"
    else:
        prediction = model.predict([[tv,radio,newspaper]])
    
    return jsonify({'predictions': prediction[0]})

@app.route('/api/v1/retrain', methods=['GET'])
def retrain():
    mse, rmse = do_train()
    return str(rmse)

app.run()