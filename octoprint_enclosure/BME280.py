import time
import board
import busio
from adafruit_htu21d import HTU21D

i2c = busio.I2C(board.SCL, board.SDA)
sensor = HTU21D(i2c)


def main():
    try:
        # Convert the data
        humidity = sensor.relative_humidity
        # Convert the data
        cTemp = sensor.temperature
        print('{0:0.1f} | {1:0.1f}'.format(cTemp, humidity))
    except:
        print('-1 | -1')

if __name__ == "__main__":
    main()
