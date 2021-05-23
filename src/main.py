import serial
import requests
import json

###
## CONFIGURATION
###
INTERFACE = "/dev/ttyUSB0"

ENTITY_ID = "sensor.prusa_print_progress"
FRIENDLY_NAME = "Prusa i3 MK3"

API_URL = "http://192.168.2.95:8123/api"
API_TOKEN = "xxxxx"

headers = {"Authorization": "Bearer " + API_TOKEN, "Content-Type": "application/json"}

###
# This functions updates the entity in Home Assistant
##
def sendToHA(percent, timeLeft):

        try:
            data = {
                    "state": percent,
                    "attributes": {
                            "unit_of_measurement": "%",
                            "friendly_name": FRIENDLY_NAME,
                            "timeLeft": timeLeft
                    }
            }

            print("Posting this to HA: " + json.dumps(data));
            r = requests.post(url = API_URL + "/states/" + ENTITY_ID, headers=headers, data=json.dumps(data))
            print(r.text)
        except:
            print("Error posting to HA. Down?")

###
# Start listening to the serial interface and read lines!
###
regex = r"NORMAL MODE: Percent done: (.*); print time remaining in mins: (.*)"

ser = serial.Serial(INTERFACE)
print(ser.name);

with serial.Serial(INTERFACE, 115200, timeout=1) as ser:
	while True:
		line = ser.readline()
		print(line)

		match = re.match(regex, line)

		if match:
			percent = match.group(1).rstrip()
			timeLeft = match.group(2).rstrip()
			sendToHA(percent, timeLeft)
