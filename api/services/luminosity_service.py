from api.sensors.bh1750_reader import BH1750Sensor #class that knows how to talk to sensor

luminositySensor = BH1750Sensor()

# return a dictionary with sensor reading
def get_luminosity_data():
	lightLevel = luminositySensor.read_luminosity()

	# return json-serializable python dictionary
	return {"luminosity_lux": lightLevel}
