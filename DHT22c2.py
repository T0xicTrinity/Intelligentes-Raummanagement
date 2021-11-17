#Autoren: Janin Hanisch & Lukas Beppler
#Projekt: Smart Hotel - Intelligentes Raummanagement


#Import von Libaries und Klassen
import datetime
import mysql.connector
import Adafruit_DHT


#Definition der Varaibalen Sensor
sensor = Adafruit_DHT.DHT22

#Definition der Variablen pin
#Der Wert steht für den GPIO-PIn an welchen der Sensor angeschlossen ist
pin = 12

#Definition eines Verbindungsstrings zur Datenbank
db = mysql.connector.connect(host="192.168.1.50", user="luft", password="luft1", database="hotel")


#Die Variablen humidity und temperature werden mit den aktuellen Sensorwerten befüllt
humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)


#Abfrage ob die Varaiblen befüllt werden konnten, d.h. ob der Sesor Werte geliefert hat
if humidity is not None and temperature is not None:

	#Ausruck der Varaibeln in Formatierung
	print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))

	#Ausdruck der rohen VAraiblen ohne Formatierung
	print (temperature)
	print (humidity)

	#Definition des Insert-Befehls für die Datenbank
	sqlStatement = ("INSERT INTO LUFTQUALITAET (sensor_ID, zeitpunkt, temperatur, luftfeuchte) VALUES (%s, %s, %s, %s)")

	#Definition der Variablen für die Befüllung der Datenbank
	val = ('NL1_1', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), round(temperature,2), round(humidity,2))

	#Erstellung eines Cursors zum Ausführen für Befhle auf der Datenbank
	cursor = db.cursor()

	#Ausführen des SQL-Statemenst auf der Datenbank
	cursor.execute(sqlStatement, val)

	#Ausführen eines Commit Befehls auf der Datenbank
	cursor.execute("COMMIT;")

#Sollten die Variablen nicht befüllt worden sein
else:
	#Ausdruck einer Fehlermeldung
	print("Failed to get reading. Try again!")
