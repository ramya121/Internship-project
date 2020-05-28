import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "jq532a"
deviceType = "raspberrypi"
deviceId = "1234567"
authMethod = "token"
authToken = "12345678"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        poll=random.randint(10, 50)
        #print(poll)
        noi =random.randint(30, 85)
        #Send Noise & polution to IBM Watson
        data = { 'Noise' : noi, 'Pollution': poll }
        #print (data)
        def myOnPublishCallback():
            print ("Published Noise = %s db" % noi, "Pollution = %s %%" % poll, "to IBM Watson")
            if noi >=70 or poll>=40:
                    print("Harmful environment")

        success = deviceCli.publishEvent("Environmental status", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
