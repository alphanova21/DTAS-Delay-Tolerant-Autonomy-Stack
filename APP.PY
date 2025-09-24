from flask import Flask
from routes import rover_bp
from database import db

app = Flask(_name_)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rover.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# register routes
app.register_blueprint(rover_bp, url_prefix="/rover")

if _name_ == "_main_":
    with app.app_context():
        db.create_all()   # create tables if not exist
    app.run(debug=True, port=5000)