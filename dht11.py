# Importeer Adafruit DHT bibliotheek.
import Adafruit_DHT
 
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
 
humidity = round(humidity, 2)
temperature = round(temperature, 2)
 
if humidity is not None and temperature is not None:
  print 'Temperatuur = {0:0.1f}*C  Luchtvochtigheid = {1:0.1f}%'.format(temperature, humidity)
else:
  print 'Kan de sensor niet uitlezen!'


