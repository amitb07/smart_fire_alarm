# Smart Fire Alarm

#### A traditional fire alarm alerts the people nearby by ringing the alarm. In case of fire accidents, time is very crucial, the sooner we inform the authorities like fire station, police station and hospital, lesser is the damage of life and property. So, to save the time, smart fire alarm itself informs the authorities when it detects fire and simultaneously rings alarm to alert people nearby. 

#### We use a Bolt IoT device which is wifi enabled microcontroller Hardware module which can interface sensors to it. The IoT device can connect to internet and can be remotely controlled using the Bolt Cloud. To detect fire at a place, we use a temperature monitoring system, when temperature reaches a certain thresold then fire is detected. LM35 sensor is used to obtain temperature readings at a place. the sensor values are temperature values to get the temperature in degree celcius, use the formula 
### Temperature in degree celcius = (100*sensor_value)/1024 

#### Every Bolt IoT device can be uniquely identified and configured using its API_KEY and DEVICE_ID at the bolt cloud. This information is added in configure.py file. 

#### To send SMS and emails, there are multiple third party SMS and email sending services which can be used. here, we are using Twilio for sending SMS and Mailgun for emails. User needs to create their account here. In twilio user will get a SID, AUTH_TOKEN and a FROM_NUMBER, this info is available on twilio dashboard which is needed in configure.py file.

#### In mailgun, user will get a mailgun_api_key and a sandbox_url available in Mailgun dashboard which will be required in the configure.py file.

#### As this is a real-time project where our IoT device needs to fetch the sensor readings at regular time interval of 10 seconds, we need our python script to run all the time and alert user in case of fire. A virtual machine is needed to run where the script can run all the time.

#### There are three entities involved in the project, the Bolt IoT hardware device, bolt cloud and the Virtual machine. The workflow is as follows:

#### 1. the virtual machine runs the python script, and requests the sensor values to the Bolt Cloud
#### 2. the Bolt Cloud identifies the device and requests the sensor value to it
#### 3. the Hardware module receives the request and sends the sensor value back to the bolt cloud.
#### 4. the bolt cloud receives sensor value and sends it to virtual machine
#### 5. the virtual machine receives the sensor value, it checks the condition to detect the fire and preforms required action accordingly
