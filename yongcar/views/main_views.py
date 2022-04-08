from flask import Blueprint, request, json, jsonify
from ..utils import predict_price

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/predict', methods=['POST'])
def predict():
     args = request.json
     model = args['model']
     age = int(args['age'])
     odo = int(args['odo'].replace(',', ''))
     color = args['color']
     fuel = args['fuel']
     print(model)
     print(age)
     print(odo)
     print(color)
     print(fuel)
     price = predict_price(model, age, odo, fuel, color)
     
     return str(price)