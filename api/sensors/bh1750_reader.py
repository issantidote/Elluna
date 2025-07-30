import board # gives access to pi i2c pins
import busio # handles i2c communication protocols
import adafruit_bh1750 # lib for bh1750

# manage bh1750 sensor
class BH1750Sensor:
	def __init__(self):

		# set up ic2 using pi's SCL and SDA pins
		i2c = busio.I2C(board.SCL, board.SDA)

		# initialize the sensor with the i2c connection
		self.sensor = adafruit_bh1750.BH1750(i2c)


	def read_luminosity(self):
		return self.sensor.lux
