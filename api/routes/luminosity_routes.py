from flask import Blueprint, jsonify #tools for grouping routes and send JSON
from api.services.luminosity_service import get_luminosity_data # pulls service function

# 'Blueprint' like a mini apii to plug into main app
luminosity_bp = Blueprint('luminosity', __name__)

# Define GET route for /luminosity
@luminosity_bp.route('/luminosity', methods=['GET'])
def read_luminosity():
	# call service function to get data from the sensor
	data = get_luminosity_data()
	return jsonify(data)
