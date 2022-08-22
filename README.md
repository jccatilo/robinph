# Welcome to ROBIN Ph's firmware repository!

1. Arduino Firmware

- Master Arduino
    - contains all the sensor data
    - responsible for identifying recyclables, sending recycleable data to Raspberry Pi via USB port, and sending commands to the slave arduino. 
    - Display

- Slave Arduino
    - connected to motors and their corresponding "fool-proofing" sensors
    - responsible for controlling motors + sending feedback to the Master arduino.

2. Python Files 

- Playing video ads

- Handling touch inputs from users

- Monitoring vital parts e.g. internet, door, main arduino