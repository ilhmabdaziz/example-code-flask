from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Parman_95@localhost:3306/test-flask?charset=utf8mb4&collation=utf8mb4_general_ci'
    app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
    }
    db.init_app(app)

    # import later on
    from routes import routes_employees,search_employee,update_data
    routes_employees(app, db)
    search_employee(app, db)
    update_data(app, db)

    migrate = Migrate(app, db)

    return app