from flask import Flask
from routes import irrigation_routes

app = Flask(__name__)
app.register_blueprint(irrigation_routes)

if __name__ == "__main__":
    app.run(debug=True)
