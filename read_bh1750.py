import time
import board
import busio
import adafruit_bh1750

# set up I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize sensor
sensor = adafruit_bh1750.BH1750(i2c)

try:
	while True:
		lux = sensor.lux
		print(f"Ambient Light: {lux:.2f} lux")
		time.sleep(1)

except KeyboardInterrupt:
	print("Stopped reading BH1750.")
