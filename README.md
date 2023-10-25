# Raspberry Pi Pico Vibration Sensor Alerts

*Get PushBullet notifications when vibrating appliances end their cycles based on their vibrations!*

Just stick your Raspberry Pi Pico & sensor onto an appliance and once it's finished you'll recieve a PushBullet notification. I use it for my washing machine but in theory it should work for any vibrating appliance.

This code makes use of the Grove Vibration Sensor (SW-420). It will detect faint shaking and once that finishes the Pi Pico will send you a notification.

## Components

* A Raspberry Pi Pico W (for wifi access)
* A wifi connection
* A Grove Vibration Sensor (SW-420)
* Any 1 amp microUSB power source to power the Pi

## Walkthrough

1. Connect the vibration sensor to the Pi Pico (an example can be seen [here](https://www.youtube.com/watch?v=twBpU_pfFbI&ab_channel=PiddlerInTheRoot))
2. Head over to [PushBullet](https://www.pushbullet.com/) to set up an account and register your device to get your auth_token and device_iden
3. Update config.py with your wifi details, PushBullet auth_token and device_iden as well as the title and body of your notification
4. Connect the Pi Pico to your computer and load the project onto it. The main.py file will now start running whenever the Pi is powered on
5. Power on the Pi with the vibration sensor attached and attach both to the appliance so its vibrations will be picked up
6. Turn the appliance on and walk away!
7. The vibrations starting will arm the Pi to listen out for a stop in the vibrations. Once the vibrations have stopped and not restarted for a full 5 minutes (300 seconds) the Pi will send you a PushBullet notificatio

