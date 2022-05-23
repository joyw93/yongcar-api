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
        data['age'] = (pd.to_datetime('now') - pd.to_datetime(data['age']+'-06-15')) / np.timedelta64(1, 'M')
        price = int(np.expm1(lgbm.predict(data))[0])
        return price