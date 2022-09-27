# Welcome to ROBIN Ph's firmware repository!

1. Arduino Firmware

    - [Master Arduino](https://github.com/jccatilo/robinph/tree/main/robin_uart_sensor)

    - contains all the sensor data

    - responsible for identifying recyclables, sending recycleable data to Raspberry Pi via USB port, and sending commands to the slave arduino.

    - Display

    - [Slave Arduino](https://github.com/jccatilo/robinph/tree/main/robin_uart_motors)

    - connected to motors and their corresponding "fool-proofing" sensors

    - responsible for controlling motors + sending feedback to the Master arduino.

2. Python Files

    - Playing video ads on loop

    - Handling touch inputs from users

    - Monitoring vital parts e.g. internet, door, main arduino

Useful links:

- [Electronic Parts Testing](https://www.tinkercad.com/things/ggsWkbZpRth-testelectronicparts)