from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile('config.py', silent=True)
    mongo.init_app(app)

    # Verificar e criar coleções se não existirem
    with app.app_context():
        db = mongo.db
        collections = db.list_collection_names()
        required_collections = ['employees', 'assets']
        for collection in required_collections:
            if collection not in collections:
                db.create_collection(collection)

    from routes.employees import employees_bp
    from routes.assets import assets_bp

    app.register_blueprint(employees_bp, url_prefix='/employees')
    app.register_blueprint(assets_bp, url_prefix='/assets')

    return app
