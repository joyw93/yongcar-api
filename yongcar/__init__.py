from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'*': {'origins': 'http://nodecar.co.kr'}})
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app