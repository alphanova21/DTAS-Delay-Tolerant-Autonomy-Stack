from flask import Flask
from routes import rover_bp

app = Flask(_name_)
app.register_blueprint(rover_bp, url_prefix="/rover")

if _name_ == "_main_":
    app.run(debug=True, port=5000)