# Welcome to ROBIN Ph's firmware repository for Mark 1

1. Arduino Firmware

    - [Master Arduino](https://github.com/jccatilo/robinph/tree/main/robin_uart_sensor)

        - connected to all the main sensors and the only arduino connected to the Raspberry Pi

        - responsible for identifying recyclables, sending recycleable data to Raspberry Pi via USB port, and sending commands to the slave arduino

        - Display on honeycomb (TBD)

    - [Slave Arduino](https://github.com/jccatilo/robinph/tree/main/robin_uart_motors)

        - connected to motors and their corresponding "fool-proofing" sensors

        - responsible for controlling motors + sending feedback to the Master arduino

2. Python Files

    - [Playing video ads on loop for 50" TV](https://github.com/jccatilo/robinph/blob/main/playvideosonloop.py)

    - [Python App to listen to arduino board via usb port](https://github.com/jccatilo/robinph/blob/main/listen_to_arduino.py)

    - [Python App to determine status of internet connection, connection to a remote server, and identifying connected devices on USB ports](https://github.com/jccatilo/robinph/blob/main/tests/main.py)

    - 7" touch screen user interface - Raspberry Pi (TBD, display unavailable)

        - should include the displaying of predetermined error codes of the machine like no internet connection, cannot connect to remote server, microcontrollers not found, recycleable jams, etc.

        - might utilize pyqt5 for UI design

    -[Bar code (in progress)](https://github.com/jccatilo/robinph/tree/main/barcode-scanner)

Useful links:

- [Electronic Parts Testing - TinkerCAD](https://www.tinkercad.com/things/ggsWkbZpRth-testelectronicparts)

- [shortcut to my folder in robin Gdrive](https://drive.google.com/drive/folders/1z0Ldyzyp_LR7B6j_t6Rcr9CUzI3i0BfU)
