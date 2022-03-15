import joblib
import pandas as pd
import numpy as np

def predict_price(model, age, odo, fuel, color):
        lgbm = joblib.load('lgbm_model.pkl')
        data = pd.DataFrame({'model': [model],
                             'age': [age],
                             'odo': [odo],
                             'fuel': [fuel],
                             'color': [color]})
        data['model'] = data['model'].astype('category')
        data['fuel'] = data['fuel'].astype('category')
        data['color'] = data['color'].astype('category')
        price = int(np.expm1(lgbm.predict(data))[0])
        return price