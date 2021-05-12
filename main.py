import configure
from boltiot import Sms, Bolt, Email
import json, time

minimum_limit = 300
maximum_limit = 600  

# connection to bolt IoT device
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
# connection to sms sender
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
# connection to email sender
mailer = Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)

while True: 
    print ("Reading sensor value")
# getting the sensor value of A0 pin from IOT device
    response = mybolt.analogRead('A0') 
# conversion of json file
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is " +str(sensor_value))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
	
            print("Making request to Mailgun to send an email")
            response = mailer.send_email("Alert", "The Current temperature sensor value is " +str(sensor_value))
            response_text = json.loads(response.text)
            print("Response received from Mailgun is: " + str(response_text['message']))
            
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)