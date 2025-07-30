from flask import Flask
from api.routes.luminosity_routes import luminosity_bp

app = Flask(__name__)
app.register_blueprint(luminosity_bp)

# @app.route("/")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

