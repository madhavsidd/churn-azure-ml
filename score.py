import json
import numpy as np
from azureml.core.model import Model
import joblib

def init():
    global model
    model_path = Model.get_model_path('churn_model')
    model = joblib.load(model_path)

def run(data):
    try:
        data = np.array(json.loads(data)['data'])
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        return str(e)